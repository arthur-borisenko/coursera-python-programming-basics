from math import sqrt


def main():
    numerator, denominator = int(input()), int(input())
    print(*ReduceFraction(numerator, denominator))
    pass


def ReduceFraction(numerator, denominator):
    GCD = getGCD(numerator, denominator)
    numerator = numerator / GCD
    denominator = denominator / GCD
    return safe_to_int(numerator), safe_to_int(denominator)


def getGCD(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    maxGCD = int(min(num2, sqrt(num1)))
    for div in range(maxGCD, 0, -1):
        if num1 % div == 0 and num2 % div == 0:
            return div


def safe_to_int(n):
    if hasattr(n, "is_integer") and n.is_integer():
        return int(n)
    else:
        return n


if __name__ == "__main__":
    main()
