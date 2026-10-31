# Pertemuan 13 - Debugging dan Testing

Nama: Aditya Setianugroho
NIM: 2225250172
Kelas: (dapat dilengkapi sesuai kelas mahasiswa)

## Kasus

Praktik ini membahas bug pada penghitungan rata-rata, batas kelulusan, dan pencarian nilai tertinggi.
Pengujian mencakup kondisi normal, batas, data kosong, serta input yang tidak valid.

## Tabel Tracing Latihan 1

Program menghitung faktorial 4.

| Langkah | i | total sebelum | total sesudah |
|---|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 2 | 2 | 1 | 2 |
| 3 | 3 | 2 | 6 |
| 4 | 4 | 6 | 24 |

## Test Case Awal

| ID | Target | Input | Expected | Actual Awal | Status |
|---|---|---|---|---|---|
| T1 | rata-rata | `[80, 60, 90, 70]` | 75.0 | 60.0 | FAIL |
| T2 | rata-rata | `[100, 80]` | 90.0 | 36.0 | FAIL |
| T3 | status | 60 | Lulus | Tidak lulus | FAIL |
| T4 | status | 59 | Tidak lulus | Tidak lulus | PASS |
| T5 | tertinggi | `[80, 60, 90, 70]` | 90 | 0 | FAIL |
| T6 | rata-rata kosong | `[]` | 0 | 0.0 | PASS* |
| T7 | tertinggi kosong | `[]` | None | 0 | FAIL |

\* Versi awal belum memeriksa data kosong dan menghasilkan pembagian nol jika dijalankan.

## Bug Report

| Bug ID | Gejala/Test | Lokasi | Akar Penyebab | Perbaikan |
|---|---|---|---|---|
| B01 | Rata-rata salah pada T1-T2 | `praktik_4_debugging.py`, `hitung_rata_rata` | Pembagi selalu bernilai 5, bukan jumlah elemen | Gunakan `len(nilai)` dan tangani list kosong |
| B02 | Nilai 60 dinyatakan tidak lulus pada T3 | `praktik_4_debugging.py`, `status` | Pembanding `> 60` tidak memasukkan nilai batas | Gunakan `>= 60` |
| B03 | Nilai tertinggi 0 pada T5 | `praktik_4_debugging.py`, `nilai_tertinggi` | Inisialisasi 0 dan pembanding terbalik (`x < tertinggi`) | Mulai dari `nilai[0]`, bandingkan `x > tertinggi`, tangani list kosong |

## Cara Menjalankan

```bash
python praktik/praktik_4_debugging.py
python latihan/03_test_case.py
```

## Refleksi

Teknik paling membantu adalah tracing dan breakpoint karena keduanya membuat perubahan nilai variabel serta alur keputusan dapat diamati secara konkret. Test case batas diperlukan untuk membuktikan bug tanpa bergantung pada perkiraan.
