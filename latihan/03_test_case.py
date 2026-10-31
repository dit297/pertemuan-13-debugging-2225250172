import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from praktik.praktik_4_debugging import hitung_rata_rata, nilai_tertinggi, status


TEST_CASES = [
    ("T1 rata-rata 4 data", lambda: hitung_rata_rata([80, 60, 90, 70]) == 75.0),
    ("T2 rata-rata 2 data", lambda: hitung_rata_rata([100, 80]) == 90.0),
    ("T3 batas kelulusan 60", lambda: status(60) == "Lulus"),
    ("T4 di bawah batas 59", lambda: status(59) == "Tidak lulus"),
    ("T5 nilai tertinggi", lambda: nilai_tertinggi([80, 60, 90, 70]) == 90),
    ("T6 list kosong rata-rata", lambda: hitung_rata_rata([]) == 0),
    ("T7 list kosong tertinggi", lambda: nilai_tertinggi([]) is None),
]


def jalankan_test():
    gagal = 0
    for nama, test in TEST_CASES:
        hasil = test()
        print(f"{nama}: {'PASS' if hasil else 'FAIL'}")
        gagal += not hasil
    return gagal


if __name__ == "__main__":
    raise SystemExit(1 if jalankan_test() else 0)
