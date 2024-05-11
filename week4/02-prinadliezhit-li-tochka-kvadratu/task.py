def main():
    x, y = float(input()), float(input())
    if IsPointInSquare(x, y):
        print("YES")
    else:
        print("NO")


def IsPointInSquare(x, y):
    return abs(x) <= 1 and abs(y) <= 1


if __name__ == "__main__":
    main()
