def get_seq():
    result = []
    n = int(input())
    while n != 0:
        result.append(n)
        n = int(input())
    return result


def main():
    seq = get_seq()
    max_el = max(seq)
    res = 0
    for el in seq:
        if el == max_el:
            res += 1
    print(res)


if __name__ == '__main__':
    main()
