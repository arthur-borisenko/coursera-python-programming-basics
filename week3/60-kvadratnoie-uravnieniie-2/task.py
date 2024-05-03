import math
from enum import Enum


class rootCounts(Enum):
    NaN = "3"
    Two = "2"
    One = "1"
    Zero = "0"


def safe_to_int(n):
    if n.is_integer():
        return int(n)
    else:
        return n


def solve_quadratic_equation(a, b, c):
    if a == 0:
        if b == 0 and c == 0:
            return rootCounts.NaN.value
        elif b == 0:
            return rootCounts.Zero.value
        else:
            return rootCounts.One.value, str(
                safe_to_int((-c) / b))
    else:
        D = b ** 2 - 4 * a * c
        if D == 0:
            x = safe_to_int(-b / (2 * a))
            return rootCounts.One.value, str(x)
        elif D > 0:
            x = safe_to_int((-b + math.sqrt(D)) / (2 * a))
            y = safe_to_int((-b - math.sqrt(D)) / (2 * a))
            return rootCounts.Two.value, min(x, y), max(x, y)
        else:
            return rootCounts.Zero.value


def main():
    a, b, c = float(input()), float(input()), float(input())
    print(
        " ".join(list(map(str, solve_quadratic_equation(a, b, c)))))


if __name__ == '__main__':
    main()
