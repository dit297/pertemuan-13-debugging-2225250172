def hitung_faktorial(n):
    total = 1
    for i in range(1, n + 1):
        total = total * i
    return total


if __name__ == "__main__":
    print(hitung_faktorial(4))
