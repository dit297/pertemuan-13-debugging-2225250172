def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


def validasi_nilai(nilai):
    return 0 <= nilai <= 100


if __name__ == "__main__":
    for nilai in (59, 60, 61, 75, 120):
        if validasi_nilai(nilai):
            print(nilai, status_lulus(nilai))
        else:
            print(nilai, "Nilai tidak valid")
