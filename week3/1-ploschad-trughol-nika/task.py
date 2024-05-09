from math import sqrt


def main():
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) * 0.5
    d = p * (p - a) * (p - b) * (p - c)
    s = sqrt(d)
    if s.is_integer():
        s = int(s)
    print(s)


if __name__ == '__main__':
    main()
