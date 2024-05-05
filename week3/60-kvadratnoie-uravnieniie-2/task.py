import math
from enum import Enum


class RootCounts(Enum):
    NaN = 3
    Two = 2
    One = 1
    Zero = 0


def safe_to_int(n):
    if hasattr(n, "is_integer") and n.is_integer():
        return int(n)
    else:
        return n


def safe_solve_quadratic_equation(a, b, c):
    if a == 0:
        if b == 0 and c == 0:
            return [RootCounts.NaN.value]
        elif b == 0:
            return [RootCounts.Zero.value]
        else:
            return [RootCounts.One.value, safe_to_int((-c) / b)]
    else:
        return solve_quadratic_equation(a, b, c)


def solve_quadratic_equation(a, b, c):
    D = b ** 2 - 4 * a * c
    if D == 0:
        x = safe_to_int(-b / (2 * a))
        return [RootCounts.One.value, x]
    elif D > 0:
        x = safe_to_int((-b + math.sqrt(D)) / (2 * a))
        y = safe_to_int((-b - math.sqrt(D)) / (2 * a))
        return [RootCounts.Two.value, min(x, y), max(x, y)]
    else:
        return [RootCounts.Zero.value]


def main():
    a, b, c = float(input()), float(input()), float(input())
    result = safe_solve_quadratic_equation(a, b, c)
    print(" ".join(map(str, map(safe_to_int, result))))


if __name__ == '__main__':
    main()
