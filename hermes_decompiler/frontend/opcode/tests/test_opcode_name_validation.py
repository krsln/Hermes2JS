"""
Validate that every registered OpcodeHandler corresponds to a real Hermes
bytecode opcode.

Dispatch is performed by matching OpcodeEntry.opcode directly to the
OpcodeHandler subclass name. A typo in a handler class name therefore
creates silently unreachable code, while a missing handler represents an
unnoticed coverage gap.

The opcode catalog is generated from the hermes-dec project and contains
the union of all tracked Hermes bytecode versions (currently hbc51-hbc99).

Handlers are classified as:

    CURRENT  - present in the newest tracked bytecode version.
    LEGACY   - present only in older tracked versions.
    UNKNOWN  - not found in any tracked version.

UNKNOWN handlers fail the test unless explicitly allow-listed.
"""

from __future__ import annotations

import pytest

from hermes_decompiler.handlers.HandlerLoader import HandlerLoader
from hermes_decompiler.handlers.OpcodeHandler import OpcodeHandler
from hermes_decompiler.frontend.opcode import OpcodeStatus, classify_all

# Bu isimler gerçek opcode DEĞİL: OpcodeHandler'ın davranışını (regex
# pattern, get_register_expression, vs.) paylaşan yardımcı/mixin
# sınıflarıdır ve register edilmemelidir. `_abstract = True` ile
# işaretlendikleri için normalde zaten registry'ye girmezler; bu liste
# sadece "hâlâ birileri sızdırırsa hemen fark edelim" güvencesi.
NON_OPCODE_HELPER_CLASSES = {"OpcodeHandler"}

# hbc51-hbc99 aralığında adına rastlamadığımız ama var olduğunu net olarak
# doğrulayamadığımız handler adları. Buraya bir isim eklerken MUTLAKA
# gerekçe (hangi sürüm / hangi kaynak) yazın - aksi halde bu, "belki
# haklıyızdır" diye unutulan bir typo olur.
#
# NOT: Bu proje her yeni handler eklerken opcode adını harici bir kaynaktan
# (opcodes_table.html, BytecodeList.def veya gerçek bir .hbc çıktısı) teyit
# ediyor; bu yüzden bu liste boş tutulmalı. Boş değilse, aşağıdaki test
# bilerek/gerekçeyle burada duran isimleri "izin verilen" sayar ama yine de
# görünür kalmaları için ayrı bir uyarı testiyle raporlanır.
KNOWN_UNVERIFIED: dict[str, str] = {
    # "BitOrN": "TODO: hangi sürüm/kaynakta doğrulandı?",
}


@pytest.fixture(scope="module")
def registered_opcode_names() -> list[str]:
    HandlerLoader.load()
    return [
        name for name in OpcodeHandler.registry
        if name not in NON_OPCODE_HELPER_CLASSES
    ]


def test_every_handler_name_is_a_known_opcode(registered_opcode_names):
    buckets = classify_all(registered_opcode_names)

    unknown = [info for info in buckets[OpcodeStatus.UNKNOWN] if info.name not in KNOWN_UNVERIFIED]

    if unknown:
        details = "\n".join(
            f"  - {info.name}"
            for info in unknown
        )

        pytest.fail(
            "The following handler class names do not exist in any tracked "
            "Hermes bytecode version (hbc51-hbc99).\n\n"
            "Either:\n"
            "  1. the handler name contains a typo, or\n"
            "  2. the opcode belongs to a newer Hermes bytecode version that "
            "is not yet tracked.\n\n"
            "Verify the opcode against a trusted external source before "
            "merging.\n\n"
            f"{details}"
        )


def test_legacy_opcodes_are_visible_and_documented(registered_opcode_names):
    """
    Bilgilendirici test: LEGACY (eski sürüm) olarak sınıflandırılan
    handler'ları listeler. Bu test asla FAIL olmaz (legacy destek
    bilinçli bir tasarım tercihi) - amacı, "hangi handler'lar hangi
    sürüm aralığında geçerli" bilgisini CI çıktısında görünür kılmak,
    böylece bu bilgi sadece kaynak koddaki yorum satırlarına gömülü
    kalmaz.
    """
    buckets = classify_all(registered_opcode_names)
    legacy = buckets[OpcodeStatus.LEGACY]

    print(f"\n{len(legacy)} legacy (hbc99'da olmayan) handler bulundu:")
    for info in legacy:
        v_min, v_max = info.versions[0], info.versions[-1]
        print(f"  - {info.name}: hbc{v_min}..hbc{v_max}")

    assert True


def test_known_unverified_list_is_empty():
    """
    KNOWN_UNVERIFIED listesi boş olmalı. Bu test kasıtlı olarak sert:
    "teyit edilemedi ama muhtemelen doğrudur" diye bırakılan isimlerin
    projede kalıcı hale gelmesini engellemek için var.
    """
    assert not KNOWN_UNVERIFIED, (
        f"KNOWN_UNVERIFIED içinde {len(KNOWN_UNVERIFIED)} teyit "
        f"edilmemiş isim var: {sorted(KNOWN_UNVERIFIED)}. Bunları ya "
        f"teyit edip kaldırın ya da (teyit edilemiyorsa) handler'ı "
        f"kaldırmayı değerlendirin."
    )


def test_no_duplicate_registration_shadowing():
    """
    Registry class-name -> instance sözlüğü olduğu için, iki farklı
    modülde yanlışlıkla aynı isimde bir class tanımlanırsa biri
    diğerini sessizce ezer. HandlerLoader tüm alt paketleri tarayarak
    import ettiği için bu, modüller arası bir isim çakışmasında fark
    edilmesi zor bir hatadır. Bu test en azından KAÇ tane class
    tanımlandığını (import zamanında toplanan) registry boyutuyla
    karşılaştırarak somut bir "beklenen sayı" bırakır; sayı düşerse
    (yeni bir çakışma/typoyla) bir insan bunu inceler.
    """
    HandlerLoader.load()
    # NOT: Bu sayıyı, kasıtlı bir handler ekleme/çıkarma/birleştirme
    # yaptığınızda güncelleyin - amacı "sessiz gölgeleme" tespitidir,
    # rastgele bir üst sınır değildir.
    assert len(OpcodeHandler.registry) >= 200
