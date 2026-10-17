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

`goto`: çıktısında `goto label_N` kalan fonksiyon sayısı. `pathdefs`: bir yolda tanımlanmadan okunan
register'ı olan fonksiyon sayısı (yaklaşık denetim).

Son goto sınıflandırması (2026-10-16, bu turdan önce): 96 farklı bölge 236 / kardeş 110 / diğer 58 /
döngü 13; 98 farklı bölge 238 / kardeş 93 / diğer 60 / döngü 22. Tek goto'lu fonksiyon sayısı: 435.

## Açık: doğruluk hataları

Çıktı yanlış ya da yanıltıcı. goto olmadığı için survey'in goto sayısında görünmezler.

- **F-01 Eski register adı.** 96/4456: `r0[0]._responderRegion = r0`; doğrusu
  `getEnvironment(0)[0]._responderRegion = r0`. `r0` sonradan yeni nesneye atanıyor ama inline edilen
  `r0[0]` ortamı kastediyordu (frontend'in doğrusal inline'ı, `LoadFromEnvironment` + sonraki atama).
  pathdefs bu sınıfı yakalamaz; başka fonksiyonlarda da olabilir. Önce yaygınlığı ölçmek gerekir.
- **F-02 Çift negasyon.** 98/9594 `Pe`: `r2 = !r2; r1 = !!r2`. Değer iki kez uygulanıyor.
  `<unresolved_typeof_mask_0x0102>` da çözülemiyor. Eskiden `|| r1 ||` diye başka yerde yanlıştı.
- **F-03 `maybeSwapComponents` (A11).** 96/9150 benzeri kalıp. Ayrıntı için
  `tests/test_shared_return_exit.py`.
- **F-04 Kurulum register'ı END'de de okunuyor.** 96/9118 `parseScaleX`: `r1 = 0` kurulumu, birleşme
  noktasında da okunuyor; katlama onu düşüremiyor ve goto kalıyor.

## Açık: goto kümeleri

- **F-10 Çıkış bloğuna koşullu atlama.** `if (c) goto sonReturn`. Paylaşılan return bloğuna giden koşullu
  atlamalar (örnekler: 96/2019 `mountDeferredValueImpl`, 98/1871 `get`, 98/11891'in bir kısmı).
  Bu turdan sonra en büyük küme.
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