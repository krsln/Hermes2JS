# scripts/audit

Çıktı kalitesini ölçen yardımcı araçlar. Hepsi repo kökünden çalıştırılır. Sayıların mutlak değerine
değil, iki koşunun karşılaştırmasına güvenilir (bkz. `docs/FINDINGS.md`, "Ölçümler").

| Araç                     | Ne yapar                                                              |
|--------------------------|-----------------------------------------------------------------------|
| `definite_assignment.py` | Her yolda atanmadan okunan register'ları bulur (`pathdefs`).          |
| `compare_outputs.py`     | İki çıktı dizinini karşılaştırır (değişen dosya, `goto`, `pathdefs`). |
| `drop_scan.py`           | Karar ağacında kaybolmuş CFG kenarlarını (sessiz kayıp) bulur.        |

Çıktı dizini: `scripts/decompile_sections.py -i <sections> -o <dizin>` ile üretilen `.js` dosyaları.

## definite_assignment.py

```shell
python3 scripts/audit/definite_assignment.py <dosya.js | dizin> [...]
```

Okunan ama her yolda atanmamış register'ları `dosya: rN  satır` olarak yazar; bulgu varsa çıkış kodu 1.
Yapılandırılmış `if/else`'e bakar; `for-of`/`for-in` başlıkları ve `switch` kolları yanlış pozitif
verir, bu yüzden iki koşuyu karşılaştırın.

`pathdefs` (bulgusu olan **fonksiyon** sayısı) için dosya adlarını tekilleştirin:

```shell
python3 scripts/audit/definite_assignment.py apps/demo/fixtures/96/results | cut -d: -f1 | sort -u | wc -l
python3 scripts/audit/definite_assignment.py apps/demo/fixtures/98/results | cut -d: -f1 | sort -u | wc -l

python3 scripts/audit/definite_assignment.py apps/testy/96/output/results | cut -d: -f1 | sort -u | wc -l
python3 scripts/audit/definite_assignment.py apps/testy/98/output/results | cut -d: -f1 | sort -u | wc -l
```

## compare_outputs.py

```shell
python3 scripts/audit/compare_outputs.py <eski-dizin> <yeni-dizin>
```

Çıktı: değişen dosya sayısı, `goto`lu dosya sayısı (önce → sonra), yeni `goto` alan ve tüm `goto`ları
kaybeden dosyalar, `pathdefs`i kötüleşen/düzelen dosyalar. Eski dizinde olmayan dosyalar atlanır ve
raporlanır. Her değişiklikten sonra tam paketlerde (96 ve 98) çalıştırın; günlükte
`N sections failed` satırına ve çıkış koduna da bakın.

## drop_scan.py

```shell
python3 scripts/audit/drop_scan.py <sections-dizini> <cikti-dizini> <sonuc.jsonl>
python3 scripts/audit/drop_scan.py --report <sonuc.jsonl>
```

Her fonksiyonda seçilen denemenin (karar ağacı, CFG) çiftini denetler: ağaçtaki bloklar arasındaki her
CFG kenarı, ağacın kendi akış grafında hâlâ bir yol olmalıdır. Kaybolan kenar, çözülmüş kodun artık
alamayacağı bir yoldur (sessiz kayıp ya da yanlış değer).

`--report`, `goto`suz ve `edge lost` bulgusu olan fonksiyonları listeler (aday listesi). Bilinen yanlış
pozitifler: yalın `return undefined`'a giden kenar, ulaşılamaz bir `catch` bloğundan çıkan kenar,
`if` kolu içindeki erken `return`. `block missing` bulguları gürültülüdür.

Tam bir paket uzun sürer; arka planda çalıştırın (`setsid nohup ... &`) ve bitiş işaretini bekleyin.