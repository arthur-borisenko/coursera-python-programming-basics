def main():
    a, b = int(input()), int(input())
    print(sum(a, b))


def sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return sum(a, b - 1) + 1


if __name__ == "__main__":
    main()
