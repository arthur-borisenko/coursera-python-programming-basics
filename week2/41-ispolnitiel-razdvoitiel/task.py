def main():
    A = int(input())
    B = int(input())
    while A != B:
        if A % 2 == 0 and A / 2 >= B:
            print(":2")
            A /= 2
        else:
            print("-1")
            A -= 1


if __name__ == '__main__':
    main()
