def hitung_diskon(total_belanja):
    if total_belanja >= 500000:
        return total_belanja * 0.10
    elif total_belanja >= 200000:
        return total_belanja * 0.05
    return 0


def hitung_ongkir(berat_kg):
    if berat_kg <= 0:
        raise ValueError("Berat harus lebih dari 0")
    if berat_kg <= 1:
        return 10000
    elif berat_kg <= 5:
        return 20000
    return 35000


def hitung_total_bayar(total_belanja, berat_kg):
    if total_belanja <= 0:
        raise ValueError("Total belanja harus lebih dari 0")
    diskon = hitung_diskon(total_belanja)
    ongkir = hitung_ongkir(berat_kg)
    return total_belanja - diskon + ongkir