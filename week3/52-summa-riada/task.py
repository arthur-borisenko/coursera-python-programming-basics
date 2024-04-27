def if_integer_than_to_int(n):
    if n.is_integer():
        n = int(n)
    return n


def main():
    n = int(input())
    prev_znam = 1
    prev_div = 1
    for num in range(2, n + 1):
        prev_znam = prev_znam * num ** 2 + prev_div
        prev_div *= num ** 2
    print(if_integer_than_to_int(prev_znam / prev_div))


if __name__ == '__main__':
    main()
