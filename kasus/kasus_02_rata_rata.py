def rata_rata(data):
    if not data:
        return 0
    return sum(data) / len(data)


if __name__ == "__main__":
    print(rata_rata([80, 90, 70]))
    print(rata_rata([80, 90]))
    print(rata_rata([]))
