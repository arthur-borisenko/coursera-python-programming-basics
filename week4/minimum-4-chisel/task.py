def main():
    a, b, c, d = int(input()), int(input()), int(input()), int(
        input())
    print(min4(a, b, c, d))


def min4(a, b, c, d):
    return min(a, min(b, min(c, d)))


if __name__ == "__main__":
    main()
