def check1(n1):
    if (n1 % 4 == 0 and n1 % 100 != 0) or n1 % 400 == 0:
        return True


def main():
    n = int(input())
    if check1(n):
        print('YES')
    else:
        print("NO")


if __name__ == '__main__':
    main()
