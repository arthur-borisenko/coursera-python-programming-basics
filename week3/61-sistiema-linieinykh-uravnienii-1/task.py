def safe_to_int(n):
    if n.is_integer():
        return int(n)
    else:
        return n


def main():
    a, b, c = float(input()), float(input()), float(input())
    d, e, f = float(input()), float(input()), float(input())
    # a_11 * x + a_12 * y = b_1
    # a_21 * x + a_22 * y = b_2
    # (from task)
    # a_11 is not zero,because system has exactly one solution
    if a == 0:
        a_11, a_12, a_21, a_22, b_1, b_2 = c, d, a, b, f, e
    else:
        a_11, a_12, a_21, a_22, b_1, b_2 = a, b, c, d, e, f
    y = (b_2 - b_1 * a_21 / a_11) / (a_22 - a_21 * a_12 / a_11)
    x = (e - b * y) / a
    print(safe_to_int(x), safe_to_int(y))


if __name__ == '__main__':
    main()
