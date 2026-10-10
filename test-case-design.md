# Test Case Design - Kasir Toko Sederhana

Kriteria: **Decision Coverage** (setiap keputusan bernilai True dan False minimal satu kali).

## Daftar Keputusan

| ID | Fungsi | Keputusan |
|----|--------|-----------|
| D1 | hitung_diskon | total_belanja >= 500000 |
| D2 | hitung_diskon | total_belanja >= 200000 |
| D3 | hitung_ongkir | berat_kg <= 0 |
| D4 | hitung_ongkir | berat_kg <= 1 |
| D5 | hitung_ongkir | berat_kg <= 5 |
| D6 | hitung_total_bayar | total_belanja <= 0 |

## Fungsi 1: hitung_diskon(total_belanja)

| Test case | Input | Expected output |
|-----------|-------|-----------------|
| TC01 | total_belanja = 600000 | 60000 (diskon 10%) |
| TC02 | total_belanja = 300000 | 15000 (diskon 5%) |
| TC03 | total_belanja = 100000 | 0 (tanpa diskon) |

## Fungsi 2: hitung_ongkir(berat_kg)

| Test case | Input | Expected output |
|-----------|-------|-----------------|
| TC04 | berat_kg = 0 | ValueError ("Berat harus lebih dari 0") |
| TC05 | berat_kg = 0.5 | 10000 |
| TC06 | berat_kg = 3 | 20000 |
| TC07 | berat_kg = 8 | 35000 |

## Fungsi 3: hitung_total_bayar(total_belanja, berat_kg)

| Test case | Input | Expected output |
|-----------|-------|-----------------|
| TC08 | total_belanja = 0, berat_kg = 2 | ValueError ("Total belanja harus lebih dari 0") |
| TC09 | total_belanja = 600000, berat_kg = 2 | 560000 (600000 - 60000 + 20000) |

## Matriks Decision Coverage

| Keputusan | True dicakup oleh | False dicakup oleh |
|-----------|-------------------|--------------------|
| D1 | TC01 | TC02, TC03 |
| D2 | TC02 | TC03 |
| D3 | TC04 | TC05, TC06, TC07 |
| D4 | TC05 | TC06, TC07 |
| D5 | TC06 | TC07 |
| D6 | TC08 | TC09 |

Hasil: semua 12 hasil keputusan (6 True dan 6 False) tercakup oleh 9 test case.
