import math


class rootCounts:
    NaN = "3"
    Two = "2"
    One = "1"
    Zero = "0"


def if_n_is_integer_convert_to_int(n):
    if n.is_integer():
        return int(n)
    else:
        return n


def calculate_roots(a, b, c):
    D = b ** 2 - 4 * a * c
    if D == 0:
        x = if_n_is_integer_convert_to_int(-b / (2 * a))
        return rootCounts.One, str(x)
    elif D > 0:
        x = if_n_is_integer_convert_to_int(
            (-b + math.sqrt(D)) / (2 * a))
        y = if_n_is_integer_convert_to_int(
            (-b - math.sqrt(D)) / (2 * a))
        return rootCounts.Two, str(min(x, y)), str(max(x, y))
    else:
        return rootCounts.Zero


def calculate_root_when_a_is_zero(b, c):
    if b == 0 and c == 0:
        return rootCounts.NaN
    elif b == 0:
        return rootCounts.Zero
    else:
        return rootCounts.One, str(
            if_n_is_integer_convert_to_int((-c) / b))


def main():
    a, b, c = float(input()), float(input()), float(input())
    if a == 0:
        print(" ".join(calculate_root_when_a_is_zero(b, c)))
    else:
        print(" ".join(calculate_roots(a, b, c)))


if __name__ == '__main__':
    main()
