import math


def calculateRoots(a, b, c):
    D = b ** 2 - 4 * a * c
    if D == 0:
        x = -b / (2 * a)
        return [x]
    elif D > 0:
        x = (-b + math.sqrt(D)) / (2 * a)
        y = (-b - math.sqrt(D)) / (2 * a)
        return [x, y]
    else:
        return []


def if_n_is_integer_convert_to_int(n):
    if n.is_integer():
        return int(n)
    return n


def main():
    roots = []
    a, b, c = float(input()), float(input()), float(input())
    roots = calculateRoots(a, b, c)
    if len(roots) == 2:
        print(if_n_is_integer_convert_to_int(min(roots)),
              if_n_is_integer_convert_to_int(max(roots)))
    elif len(roots) == 1:
        print(if_n_is_integer_convert_to_int(roots[0]))


if __name__ == '__main__':
    main()
