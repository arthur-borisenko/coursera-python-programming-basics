def safe_to_int(n):
    if n.is_integer():
        return int(n)
    else:
        return n


def main():
    a, b, c, d, e, f = float(input()), float(input()), float(
        input()), float(
        input()), float(input()), float(input())
    if a == 0:
        a, b, c, d, e, f = c, d, a, b, f, e
    y = (f - e * c / a) / (d - c * b / a)
    x = (e - b * y) / a
    print(safe_to_int(x), safe_to_int(y))


if __name__ == '__main__':
    main()
