def if_integer_than_to_int(n):
    if n.is_integer():
        n = int(n)
    return n


def main():
    n = int(input())
    prev_numerator = 1
    prev_denominator = 1
    for num in range(2, n + 1):
        prev_numerator = prev_numerator * num ** 2 + prev_denominator
        prev_denominator *= num ** 2
    print(if_integer_than_to_int(prev_numerator / prev_denominator))


if __name__ == '__main__':
    main()
