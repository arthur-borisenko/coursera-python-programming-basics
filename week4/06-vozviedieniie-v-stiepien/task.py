def safe_to_int(n):
    if hasattr(n, "is_integer") and n.is_integer():
        return int(n)
    else:
        return n


def power(a, n):
    if n > 0:
        return power(a, n - 1) * a
    else:
        return 1


def main():
    a, n = float(input()), int(input())
    print(safe_to_int(power(a, n)))


if __name__ == "__main__":
    main()
