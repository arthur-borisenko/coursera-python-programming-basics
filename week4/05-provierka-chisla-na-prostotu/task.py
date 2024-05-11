from math import sqrt


def main():
    n = int(input())
    if IsPrime(n):
        print("YES")
    else:
        print("NO")


def IsPrime(n):
    return MinDivisor(n) == n


def MinDivisor(n):
    maximum = sqrt(n)
    current = 2
    while current <= maximum:
        if n % current == 0:
            return current
        current += 1
    return n


if __name__ == "__main__":
    main()
