# Bulgular

Açık ve çözülmüş decompiler bulguları. Her kaydın bir kimliği (`F-n`), durumu, örnek fonksiyonu (`<paket>/<fonksiyon>`:
96 ve 98 test paketleridir), tek cümlelik belirtisi ve ilgili test ya da
fixture adı vardır. Commit mesajlarında ve testlerde `F-n` diye anılabilir.

Güncelleme yöntemi: bir bulgu çözülünce "Açık"tan "Çözüldü"ye taşınır, silinmez. Aynı sınıf hata geri
gelirse nereden bakılacağı görünsün diye test adı ve commit hash'i yazılır.

## Ölçümler

Her turdan sonra bu satır güncellenir. Ölçüm: iki paketin tüm fonksiyonları üzerinde survey.

| Tarih                 | goto (96) | goto (98) | pathdefs (96) | pathdefs (98) | Test      |
|-----------------------|-----------|-----------|---------------|---------------|-----------|
| 2026-10-16 (tur başı) | 417       | 413       | 160           | 193           | 954 geçti |
| 2026-10-17            | 396       | 402       | 160           | 193           | 957 geçti |
| 2026-10-17 (F-01/F-02)| 396       | 400       | ölçülmedi     | ölçülmedi     | 985 geçti |
| 2026-10-18 (F-10 kısmi)| 383      | 392       | ölçülmedi     | ölçülmedi     | 987 geçti |
| 2026-10-18 (F-114)    | 383       | 385       | ölçülmedi     | ölçülmedi     | 988 geçti |
| 2026-10-18 (F-115)    | 383       | 385       | ölçülmedi     | ölçülmedi     | 989 geçti |
| 2026-10-18 (F-116)    | 383       | 385       | ölçülmedi     | ölçülmedi     | 990 geçti |
| 2026-10-18 (F-117)    | 358       | 372       | ölçülmedi     | ölçülmedi     | 992 geçti |
| 2026-10-19 (F-118)    | 359       | 372       | ölçülmedi     | ölçülmedi     | 994 geçti |
| 2026-10-20 (F-119)    | 349       | 366       | ölçülmedi     | ölçülmedi     | 996 geçti |

`goto`: çıktısında `goto label_N` kalan fonksiyon sayısı. `pathdefs`: bir yolda tanımlanmadan okunan
register'ı olan fonksiyon sayısı (yaklaşık denetim; survey aracı repoda yok, son satırda ölçülmedi).

Son goto sınıflandırması (2026-10-16, bu turdan önce): 96 farklı bölge 236 / kardeş 110 / diğer 58 /
döngü 13; 98 farklı bölge 238 / kardeş 93 / diğer 60 / döngü 22. Tek goto'lu fonksiyon sayısı: 435.

## Açık: doğruluk hataları

Çıktı yanlış ya da yanıltıcı. goto olmadığı için survey'in goto sayısında görünmezler.

- **F-03 `maybeSwapComponents` (A11).** 96/9150 benzeri kalıp. Ayrıntı için
  `tests/test_shared_return_exit.py`. 2026-10-17: 96/9150'nin kendisi doğru çıkıyor (goto yok, iki
  `return param1`, takas yolu doğru); benzer bir örnek bulunursa buraya eklenir, yoksa kapatılabilir.
- **F-04 `parseScaleX` goto'su.** 96/9118: yanlış callee düzeldi (F-111); kalan sorun
  `if (r0) goto label_44` ("target IS a sibling in the same region"). Kurulum register'ı (`r1 = 0`)
  birleşme noktasında da okunduğu için katlama onu düşüremiyor.

## Açık: goto kümeleri

- **F-10 Çıkış bloğuna koşullu atlama.** `if (c) goto sonReturn`. Paylaşılan return bloğuna giden koşullu
  atlamalar (örnekler: 96/2019 `mountDeferredValueImpl`, 98/1871 `get`, 98/11891'in bir kısmı).
  KISMEN ÇÖZÜLDÜ (bkz. F-113): yalnız `return`/`throw` (+ sabit yükleme) kuyrukları. Kalanlar:
  (a) ifade içeren kuyruklar çözüldü (F-117); (b) 96/11046: dönüş register'ı yola göre farklı değer taşıyor (phi), goto olarak kalıyor;
  (c) 98/1871 çözüldü (F-114); (e) exception handler'lı fonksiyonlar çözüldü (F-119); (d) hedefi return olmayan (kardeş bölge,
  `none` sonlandırıcı) atlamalar. 96/4846 ve 96/10300 `binarySubdivide` döngüyle taşınan `r10` hatası çözüldü (F-115).
- **F-11 `try/finally` içinde goto.** 98/2007 `preprocessException`, 98/10013 `flush`, 96/840.
  Atlamanın `finally` sınırını geçmesi.
- **F-12 `await`/`yield` dispatch ve 98 generator opcode'ları.** 96/12207 `_anon_0`. Batch tablosu olmadan
  dispatch çözülemiyor; 98'de bazı generator opcode'ları eksik.
- **F-13 İki latch'li döngüler.** "expected exactly one latch" uyarısı; 96'da 13, 98'de 22 fonksiyon.
- **F-14 `for-of` generator açılımı.** Döngü, generator açılımı olarak kalıyor.
- **F-15 Paylaşılan kuyruk return'leri.** 96/10216.
- **F-16 Sabit kurulumun `Ret` tarafından okunması.** 96/150 `ve`: kurulumdaki `r0 = undefined`,
  `Ret r0` tarafından okunduğu için ilk `typeof` testi `||` zincirine katılamıyor (çıktı doğru ama iç içe).
- **F-17 `getStateForAction`.** 96/7152: büyük ve zaten goto'lu; pathdefs işareti kabul edilmiş durumda.
  Ayrı ele alınmadıkça atlanır.
- **F-18 "Farklı bölge" uzun kuyruk.** Kalan ~230 fonksiyonda tek bir ortak neden yok; küçük örneklerden (tek goto, 26
  satırdan kısa: 79 fonksiyon) başlamak en ucuzu.

## Açık: okunabilirlik

- **F-30** Döngü koşulunda `i < r8; r8 = r8.length`.
- **F-31** Gereksiz kopyalar (`r2 = r3`, `r1 = {...}; r0 = r1`).
- **F-32** Üçlü koşulun testinde fazladan parantez: `(("get" in r4) ? …)`.
- **F-33** Boş `else`/`try` gövdeleri (örnek: 98/13768 `try { } catch`).

## Çözüldü

- **F-100 Sessiz düşme** (96/652, `_interopDefault`; 96/15102, 98/167). Son test kalıbı kendi son
  testini kaybediyordu; ShortCircuit crossed formu ve `SharedTailDuplicationCfgPass`. Test:
  `tests/test_shared_tail_conditions.py`.
- **F-101 Değer üreten üçlü ve `||`/`&&` değeri yalnızca test ediliyorsa** (96/12188). Yeni
  `ValueConditionFoldCfgPass`: değer elması, ShortCircuit'ten önce tek bloğa iniyor. 8dda5b3.
- **F-102 Aynı hedefli, kurulumlu `||` zincirleri** (96/4456, 96/150). `LoadParam` gibi kurulumlar zinciri
  bölüyordu. Sabit karşılaştırma yalnızca aynı değerin tekrar karşılaştırılmasıysa `case` sayılıyor.
  c533987.
- **F-103 Koşulda çağrı varken crossed katlama** (98/11891). Kurulumdaki çağrı koşulda en solda ise
  sıra korunduğu için kabul ediliyor. c533987.
- **F-104 Artık okunmayan saf kurulum** (96/4543). Adı çözülmüş `getEnvironment(0)` katlamayı engelliyordu.
  c533987.
- **F-105 Kimlik-duyarlı ikame.** Başka komuttan inline edilmiş alt ağaçtaki register adları, katlamada
  o komutun kendi durumuyla çözülüyor. Üç yanlış çıktı düzeldi: 96/11316 `.value.value`, 96/9150
  `in r0[1][1]`, 96/9595 `undefined.deepEqual`. Ayrıca 96/3414'te `r1 === ""` kolu düşüyordu.
  c533987.
- **F-106 `repoint_references` bölge filtresi.** Katlamadan önceki bölgelerin koşulları, sonradan
  tanımlanan register'ın değeri sanılıp yeniden yönlendiriliyordu (98/2463 `r6 ||`). 8dda5b3.
- **F-107 98/2917 çökmesi.** Handler'lı fonksiyonda kenar bloğu ekleyince `compute_dominators`
  `KeyError` veriyordu; handler'lı fonksiyonda kenar bloğu eklenmiyor. d5c83ad.
- **F-108 De Morgan yazdırması.** `!(a && !b)` → `!a || b`; yalnızca printer'da, yalnızca
  `&&`/`||` içinde ve yalnızca eşitlik çevrimleri için (NaN-güvenli). 8dda5b3.
- **F-109 `TypeOfIs`/`JmpTypeOfIs` bit eşlemesi** (F-02'nin bir parçası; 98/9594). Eşleme tahmindi
  (`TYPEOF_FLAGS`/`_TYPE_BITS`); `hermesc` ile ölçüldü: undefined=1, null=2, string=4, symbol=8,
  boolean=16, number=32, bigint=64, function=128, object=256 (`typeof x === "object"` = 258, tersi 253).
  Ortak çözücü `frontend/handlers/shared/_typeof_mask.py`; çoğunluk maskeleri tümleyen olarak
  yazılıyor (`typeof x !== "object"`). 98'de 667 fonksiyonun çıktısı değişti (115'inde
  `<unresolved_typeof_mask_…>` vardı); 96'da bu opcode'lar yok. Test: `tests/test_typeof_mask.py`.
- **F-110 Printer: De Morgan çevrilen `!` yanlış gruplanıyordu** (F-02'nin diğer parçası). Üst düğüm
  `!(a && b)`'yi hâlâ `!` sanıp parantez koymuyordu: `!!(…)` değeri değiştiriyor,
  `!(a && b) && c` → `P || Q && c` oluyordu. 96'da 9, 98'de 6 fonksiyon.
  Test: `tests/test_printer_negation_grouping.py`.
- **F-111 Bayat inline okuma** (F-01; 96/4456, 96/9118, 98/12478, 98/13745, 98/9542...). `r1 = r0[0]`
  okuyucusuna inline edilirken `r0`'ın sonraki tanımının basılıp basılmayacağı o an bilinmiyordu. Scratch
  geçişi artık basılan tanımları (`printed_definitions`) toplayıp gerçek geçişe veriyor. Yaygınlık:
  96'da 1571, 98'de 1079 fonksiyonun çıktısı değişti; değişenlerin ~%94'ünde eski çıktıda
  okunan register'a hemen öncesinde basılmış bir atama var. Goto sayısı değişmedi. 13 golden fonksiyonu
  (26 dosya) yenilendi; tek tek bakılanlarda eski çıktı bayat okuma içeriyordu. Test: `tests/test_stale_inlined_read.py`.
- **F-112 Çıplak register callee üyelikle değişince `this` değişiyordu.** `r4(x)` içindeki `r4`, katlamada
  `env[1]` ile değişince `env[1](x)` (this=env) oluyordu; artık `env[1].call(undefined, x)`
  (`keep_call_this_unbound`). 98/11891 ve 98/10829. Test: `tests/test_stale_inlined_read.py`.
- **F-113 Paylaşılan çıkışın genişletilmiş kopyası** (F-10'un bir parçası; 96/10518, 98/4916, 96/2266, 98/2768,
  96/169 ...). Goto kalırsa üçüncü bir deneme (`SharedReturnDuplicationCfgPass(widen=True)`) `throw` çıkışlarını ve
  başka bir bloğun düştüğü kapanış `return`'ünü de kopyalar; yalnızca kuyruğun okuduğu her register'ın
  her yoldan tek değere ulaştığı durumda (`_reads_the_same_on_every_path`) ve yalnız goto'suz sonuç
  kabul edilir. 21 fonksiyon goto'dan çıktı (96: 396→383, 98: 400→392). İfade içeren kuyruk kopyası denendi,
  58 fonksiyon düzeltiyordu ama 96/9349'da yanlış sonuç verdi; eklenmedi. Test: `tests/test_shared_return_widened.py`.
- **F-114 Çok bloklu paylaşılan kuyruk** (F-10'un bir parçası; 98/1871 `get`, 98/1872 `getEnforcing`, 98/244, 98/249,
  98/360, 98/408, 98/6251). `a != null ? a(p) : null` ardından `?? (m[p] ?? null)`: ikinci işlenen iç testi olan
  iki bloklu bir kuyruk; bir test ona atlıyor, bir başkası düşüyor. `SharedTailDuplicationCfgPass(regions=True)` bu
  küçük ileri bölgeyi (<=4 blok, <=12 komut, tek çıkış `END`) düşen teste kopyalar. Yalnız son çare olan üçüncü
  denemede çalışır: her denemede açıkken goto'suz fonksiyonlarda `||`/`&&` zincirini bozdu (96/7424) ve 98/14169'da
  `max/min` sıkıştırmasını goto'ya çevirdi. 98: 392→385. Test: `tests/test_shared_return_widened.py`.
- **F-115 Kolda yazılan kopya, birleşimden sonra tek tanım sanılıyordu** (96/4846, 96/10300, 98/12079 `binarySubdivide`;
  ayrıca 96/12935 `isArrayish`, 98/2503 `getNextLanes`, 98/8193 `compareIdentifiers` ... 20 fonksiyon). `r14 = r0; if (c) {
  r14 = param3 }; r10 = r14`: koldaki `Mov r14, r13` değerini (`param3`) `Mov r13, r10` de aynı düğüm olarak tuttuğu
  için `UnfoldedMergeRepairPass` "belirsiz" deyip onarmıyor, okuyucu `r10 = param3` basıyordu (`c` yanlışsa
  `r0` olmalıydı). Değeri kolun kendi kaynağı olan `Mov` artık sayılmıyor (`_is_source_mov_of`). Genel bir
  `is_join_value` koruması denendi, 10 test (ternary/varsayılan birleşim katlamaları) bozulduğu için bırakıldı.
  `isArrayish` testi `r0 = r3` (yolda hiç yazılmamış global nesne) yerine `r0 = r1` bekliyor. Çıktı değişen 20
  fonksiyonun hepsi aynı kalıp (eksik atama basılıyor, okuma register'a dönüyor). Test: `tests/test_shared_return_widened.py`.
  96/12935'teki kalan yol F-116'da.
- **F-116 Zincirli `Mov` okuyucuları ve kolun varsayılanı** (96/12935, 98/6200 `isArrayish`; ~50 fonksiyonun çıktısı
  değişti). `r2 = a instanceof F` (test içinde satır içi) / kolda `r2 = r3`, ardından `Mov r1, r2`, `Mov r0, r1`:
  `UnfoldedMergeRepairPass` okuyucunun ardındaki `Mov`'u (`Mov r0, r1`) da aynı düğümü tutan "başka sahip" sayıp
  onarmıyordu; `instanceof` doğru yolunda `r1` global nesneyi okuyordu. Artık okuyucunun register'ını sonradan
  kopyalayan `Mov`'lar (`_chained_reader_movs`; döngüde okuyucudan ÖNCEKİ `Mov` hariç) zincir sayılıyor. Ayrıca
  "kolda yazılan register `if`'ten sonra adıyla okunuyor" dalı, `if`'in kendi testinin satır içi aldığı varsayılanı
  (`r1 = len >= 0`) basmıyordu; `_reprint_unprinted_default` oraya da eklendi. Sonuç: `length < 0` yolunda
  `r1` atanıyor. Etki: yaklaşık 50 fonksiyonda eksik atama basılıyor / ölü varsayılan (`r0 = param1`) kalkıyor /
  `return param1` yerine `return r0` (96/1666, 98/2360 `diffProperties`). Örneklenen on kadarı bytecode ile
  karşılaştırıldı; tümü tek tek doğrulanmadı. Test: `tests/test_boolean_chain_copy_reads_register.py`.
- **F-117 İfade içeren paylaşılan kuyruk** (F-10'un bir parçası; 96/2019, 96/12456, 96/13816, 98/8735 ... 38 fonksiyon).
  `SharedReturnDuplicationCfgPass(statements=True)`: üç denemeden sonra hâlâ goto varsa dördüncü deneme, 6 komuta
  kadar sıradan komut içeren `return`/`throw` kuyruğunu da (path-bağımsızlık korumasıyla) atlayana kopyalar.
  96: 383→358, 98: 385→372, geriye giden fonksiyon yok. ÖNEMLİ: kopya komutların `value`/`statement` düğümleri derin
  kopyalanmalı; paylaşılınca bir katlama atamayı kopyadan alıyordu (96/12456: `!param1` kolu atanmamış `r1` döndürdü).
  Önceki turda bu yüzden "yanlış sonuç" gördüm, ama 96/9349 `cmp` kuyruktan bağımsız bozuk (F-118). Çıktılarda
  "her yolda atanmamış register okuması" denetimi (kaba, yapısal if/else) yalnız önceden bozuk olanları işaretledi.
  Testler: `tests/test_shared_return_widened.py`.
- **F-118 Ardışık ikili ternary'ler birbirine karışıyor** (96/9349 `cmp`, `===`/`!==` kolları). `r1 = typeof a !== "object"
  ? a : a.version; r0 = typeof c !== "object" ? c : c.version; return r1 === r0`: aynı `typeof` register'ı (`r3`) iki
  kez kullanılınca ilk ifade ikincinin testini (`(r1 !== "object") ? param1 : ...`) ve okunmamış register'ları
  taşıyor; `return` yanlış `r0` okuyor. goto'dan bağımsız (baseline'da da var).
  **Kısmen çözüldü.** `ConditionalExpressionRegionPass`: ternary'nin testindeki register, dal ile okuyan arasında
  (akış üzerinde) yeniden *yazdırılan* bir tanımla değişiyorsa okuyan ternary'nin kopyasını değil o register'ı okur
  (`repoint_references(..., reader_value=)`); register'ın o noktada dolu olduğu kanıtlanamazsa birleştirme, arm
  emilmeden ÖNCE (`_peek_arm_result`) katlanmaz. Okuyanlarına katlanıp hiç yazdırılmayan bir yazım (96/8499'daki
  `Mov r3, r1`, 98/9485'teki `r3 = console.log`) ve okuyanın kendisi YAZDIRILAN bir yeniden tanım sayılmaz: kopya
  metinde hâlâ doğru okur. İki kademe: yazdırılan yeniden tanım → register okunur (güvenli değilse katlanmaz);
  yalnız katlanmış yazım → register, ancak ikisi de sağlanıyorsa (arada ezilmemiş + katlanan ifade okuyandan önce
  çalışıyor ya da önceden yazdırılan bir varsayılan var; `_register_holds_merge`) okunur, aksi halde kopya kalır
  (96/8499'da `r1` ezildiği için kopya). Böylece 98/9485, 9486, 9490 hep `console.log(200, r6, r5)` biçiminde,
  tutarlı. Tam paket (96+98): ~286 fonksiyon değişti (96: 126, 98: 160), goto 96: 358→359 (96/12624: eski
  `r1 = (r2 !== "object") ? "object" : r4.params` bir `||` zincirini yutuyordu, yeni çıktı sadık ama goto'lu), 98:
  372. Örnekler: 96/10194 yanlış `!r0` testi → `r8`; 98/9490 `r5.retries`/`r5.name` kopyaları yazdırılan
  `r5 = getParentEnvironment(0)`'dan sonra okunuyordu (golden güncellendi). **Açık:** 96/9349 `cmp` tam fonksiyonu (switch içinde
  boş `if {} else {}` kolları, `return r3 === r1`) kuyruk/ternary'den bağımsız bozuk, baseline'da da vardı; loop
  koşullarındaki kopyalar (96/12561 örüntüsü) bu geçişten geçmiyor.
- **F-119 Exception handler'lı fonksiyonlarda paylaşılan çıkış kopyası** (F-10'un bir parçası; 96/3900
  `normalizeRootMargin`, 96/1363, 96/10844, 96/12298, 96/2813, 96/4231, 96/1907, 96/2413, 96/8034, 96/9338,
  98/11643, 98/1635, 98/2811, 98/3382, 98/5884, 98/8176 - 16 fonksiyon). `SharedReturnDuplicationCfgPass`
  fonksiyonda herhangi bir exception handler varsa hiç çalışmıyordu; bir `for-of` bile handler getirdiği için
  baştaki `if (c) return X` çıkışları `goto` kalıyordu. Artık yalnız korunan aralıktaki bloklar ve handler girişleri
  atlanır (kopya her zaman aralık dışına konur). Handler'lı fonksiyonlarda yol-bağımsızlık denetimi
  (`_reads_the_same_on_every_path`) seviye 1'de de uygulanır: yoksa 98/2477 `getComponentNameFromType`
  `r1 = null` / `r1 = displayName || ...` phi'sini `return null`'a çeviriyordu. Denediğim ve ATTIĞIM: "her
  atlayana kopya, orijinal ölür" (`every_jumper`, seviye 5) - 96/10211'de `if (A) {} else if (B) {} r0 = true`
  gibi yanlış çıktı üretti. Tam paket: goto 96: 359→349, 98: 372→366; başka çıktı değişmedi.