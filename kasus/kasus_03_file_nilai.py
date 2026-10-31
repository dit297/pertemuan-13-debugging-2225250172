from pathlib import Path


def baca_nilai(path):
    try:
        with Path(path).open("r", encoding="utf-8") as file:
            nilai = []
            for baris in file:
                teks = baris.strip()
                if teks:
                    nilai.append(float(teks))
            return nilai
    except FileNotFoundError:
        return []
    except ValueError as error:
        raise ValueError("File memuat nilai yang tidak valid") from error


if __name__ == "__main__":
    data = baca_nilai("data/nilai.txt")
    print(data)
