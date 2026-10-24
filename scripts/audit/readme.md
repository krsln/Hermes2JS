# 
```shell
python3 scripts/audit/definite_assignment.py <dosya.js | dizin>
python3 scripts/audit/compare_outputs.py <eski-dizin> <yeni-dizin>
python3 scripts/audit/drop_scan.py <sections-dizini> <cikti-dizini> <sonuc.jsonl>
python3 scripts/audit/drop_scan.py --report <sonuc.jsonl>

# definite_assignment
#--------------------------------------------
python3 scripts/audit/definite_assignment.py apps/demo/fixtures/96/results | cut -d: -f1 | sort -u | wc -l
python3 scripts/audit/definite_assignment.py apps/demo/fixtures/98/results | cut -d: -f1 | sort -u | wc -l

python3 scripts/audit/definite_assignment.py apps/testy/96/output/results | cut -d: -f1 | sort -u | wc -l
python3 scripts/audit/definite_assignment.py apps/testy/98/output/results | cut -d: -f1 | sort -u | wc -l

#--------------------------------------------
```