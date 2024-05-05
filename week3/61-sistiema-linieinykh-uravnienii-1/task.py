def safe_to_int(n):
    if n.is_integer():
        return int(n)
    else:
        return n


def main():
    a, b, c, d, e, f = float(input()), float(input()), float(input()), float(
        input()), float(input()), float(input())
    x, y = None, None
    if a == 0:
        if b != 0:
            y = e / b
    elif b == 0:
        if a != 0:
            x = e / a
    if c == 0:
        if d != 0:
            y = f / d
    elif d == 0:
        if c != 0:
            x = f / c
    if x is None and y is None:
        if c * b != 0 or d * a != 0:
            x = (f * b - d * e) / (c * b - d * a)
            y = (e - a * x) / b
    if x is None and y is not None:
        if a != 0 and b != 0:
            x = (e - b * y) / a
        elif c != 0 and d != 0:
            x = (f - d * y) / c
    if y is None and x is not None:
        if a != 0 and b != 0:
            y = (e - a * x) / b
        elif c != 0 and d != 0:
            y = (f - c * x) / d
    print(safe_to_int(x), safe_to_int(y))


if __name__ == '__main__':
    main()
