# Kasir Toko Sederhana

Memenuhi Tugas Pertemuan 5 Mata Kuliah Analisis dan Pengujian Sistem (High Order Testing).

Mini program Python untuk menghitung diskon, ongkir, dan total bayar. Test case dirancang dengan kriteria **Decision Coverage**, lalu diimplementasikan sebagai unit test.

## Aturan Program

- Diskon: belanja >= 500.000 dapat 10%, belanja >= 200.000 dapat 5%, selain itu 0%
- Ongkir: berat <= 1 kg Rp10.000, berat <= 5 kg Rp20.000, berat > 5 kg Rp35.000
- Total belanja harus lebih dari 0, berat harus lebih dari 0
- Total bayar = total belanja - diskon + ongkir

## Struktur Repository

| File | Isi |
|------|-----|
| `kasir.py` | Program utama (3 fungsi) |
| `test_kasir.py` | 9 unit test menggunakan `unittest` |
| `test-case-design.md` | Test Case Design (format Myers) dan matriks decision coverage |

## Cara Menjalankan

```
python -m unittest -v test_kasir
```

Cek decision coverage:

```
python -m pip install coverage
python -m coverage run --branch -m unittest test_kasir
python -m coverage report -m --include=kasir.py
```

## Hasil

- 9 unit test lulus (Ran 9 tests, OK)
- Decision coverage 100% (6 keputusan, 12 cabang, semua tercakup)