def main():
    A, B = int(input()), int(input())
    if A <= B:
        print(*range(A, B + 1))
    else:
        print(*range(A, B - 1, -1))


if __name__ == "__main__":
    main()
