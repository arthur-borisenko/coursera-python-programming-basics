import math


def main():
    h, a, b = int(input()), int(input()), int(input())
    if a > h:
        print(1)
    else:
        print(math.ceil((h - a) / (a - b)) + 1)


if __name__ == '__main__':
    main()
