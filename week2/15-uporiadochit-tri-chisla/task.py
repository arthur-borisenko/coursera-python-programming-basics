def main():
    a, b, c = int(input()), int(input()), int(input())
    if a > b:
        (a, b) = (b, a)
    if b > c:
        (b, c) = (c, b)
        if a > b:
            (a, b) = (b, a)
    print(a, b, c)


if __name__ == '__main__':
    main()
