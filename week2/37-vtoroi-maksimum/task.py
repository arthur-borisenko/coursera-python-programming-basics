def main():
    seq = get_seq()
    res = get_top_2_element(seq)
    print(res)


def get_max(iterable):
    max_el = None
    for el in iterable:
        if max_el is None or max_el < el:
            max_el = el
    return max_el


def get_top_2_element(seq):
    seq.remove(max(seq))
    return max(seq)


def get_seq():
    result = []
    n = int(input())
    while n != 0:
        result.append(n)
        n = int(input())
    return result


if __name__ == '__main__':
    main()
