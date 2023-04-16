from math import ceil


def main():
    y = int(input())
    z = int(input())
    x = int(input())
    k = 2
    if x < y:
        r = 2
    elif x % y == 0:
        r = int(x / y * 2)
    else:
        basic = (x // y - 1) * 2
        p = x % y
        xx = 2 * p
        r = ceil(xx / y) + basic + k
    print(r * z)


if __name__ == '__main__':
    main()
