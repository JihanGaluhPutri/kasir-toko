import unittest

from kasir import hitung_diskon, hitung_ongkir, hitung_total_bayar


class TestHitungDiskon(unittest.TestCase):
    def test_TC01_diskon_10_persen(self):
        self.assertAlmostEqual(hitung_diskon(600000), 60000)

    def test_TC02_diskon_5_persen(self):
        self.assertAlmostEqual(hitung_diskon(300000), 15000)

    def test_TC03_tanpa_diskon(self):
        self.assertEqual(hitung_diskon(100000), 0)


class TestHitungOngkir(unittest.TestCase):
    def test_TC04_berat_nol_error(self):
        with self.assertRaises(ValueError):
            hitung_ongkir(0)

    def test_TC05_ongkir_ringan(self):
        self.assertEqual(hitung_ongkir(0.5), 10000)

    def test_TC06_ongkir_sedang(self):
        self.assertEqual(hitung_ongkir(3), 20000)

    def test_TC07_ongkir_berat(self):
        self.assertEqual(hitung_ongkir(8), 35000)


class TestHitungTotalBayar(unittest.TestCase):
    def test_TC08_total_belanja_nol_error(self):
        with self.assertRaises(ValueError):
            hitung_total_bayar(0, 2)

    def test_TC09_total_bayar_normal(self):
        self.assertAlmostEqual(hitung_total_bayar(600000, 2), 560000)


if __name__ == "__main__":
    unittest.main(verbosity=2)