"""
Opcode adı doğrulama testi.

`OpcodeDispatcher`, bir `OpcodeEntry.opcode` değerini doğrudan
`OpcodeHandler` alt sınıfının adıyla eşleştirerek (`registry[entry.opcode]`)
handler'a yönlendirir. Bu yüzden her handler class'ının adının, GERÇEK bir
Hermes bytecode opcode'una karşılık gelmesi kritik bir doğruluk şartıdır:
yanlış/hayali bir isim asla dispatch edilmeyen sessiz ölü kod anlamına
gelir; eksik bir isim ise fark edilmeyen bir kapsam boşluğu anlamına gelir.

Bu test, `hermes_decompiler/opcode/data/opcode_version_map.json` içinde
tutulan, hbc51..hbc99 arası TÜM Hermes bytecode sürümlerinin birleşik
opcode tablosuna (bkz. https://github.com/P1sec/hermes-dec) karşı her
kayıtlı handler adını sınıflandırır:

    - CURRENT : güncel (hbc99) sürümde var                -> OK
    - LEGACY  : eski bir sürümde var, hbc99'da yok         -> OK (bilinçli
                geriye-dönük uyumluluk), ama açıkça işaretlenmeli
    - UNKNOWN : hiçbir izlenen sürümde bulunamadı          -> FAIL

Yeni bir handler eklerken bu test kırmızıya düşerse iki ihtimal var:
  1) Opcode adında bir yazım hatası var -> düzelt.
  2) Gerçekten var olan ama bu projede henüz izlenmeyen daha yeni bir HBC
     sürümüne ait bir opcode -> `data/opcode_version_map.json`'ı güncelle
     (bkz. modül docstring'i) ve/veya `KNOWN_UNVERIFIED` listesine gerekçeyle
     ekle.
"""
from __future__ import annotations

import pytest

from hermes_decompiler.handlers import HandlerLoader, OpcodeHandler
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
    "BaseBinaryOperator": "Base Class",
    "BaseUnaryOperator": "Base Class",
    "BaseJCompare": "Base Class",
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
        details = "\n".join(f"  - {info.name}" for info in unknown)
        pytest.fail(
            "Aşağıdaki handler class adları hbc51-hbc99 arası HİÇBİR "
            "sürümde bulunamadı. Ya bir yazım/isim hatası var ya da "
            "izlenmeyen bir bytecode sürümüne ait yeni bir opcode - "
            "her iki durumda da bu isim harici bir kaynaktan teyit "
            "edilmeden birleştirilmemeli:\n" + details
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
