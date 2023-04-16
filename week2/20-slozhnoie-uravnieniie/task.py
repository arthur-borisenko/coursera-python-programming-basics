def main():
    a, b, c, d = int(input()), int(input()), int(input()), int(input())
    if c == 0 and d == 0:
        print('NO')
    elif a == 0:
        print('INF')
    else:
        x = -b / a
        if c * x + d == 0 or x % 1 != 0:
            print('NO')
        else:
            print(int(x))


if __name__ == '__main__':
    main()
