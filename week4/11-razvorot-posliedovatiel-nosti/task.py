def main():
    reverseInputStream(int(input()))


def reverseInputStream(n):
    if n != 0:
        reverseInputStream(int(input()))
    print(n)


if __name__ == "__main__":
    main()
