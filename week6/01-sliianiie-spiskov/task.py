def main():
    a = input().split()
    print(*merge(a, input().split()))
    pass


def merge(a, b):
    """
    merge two sorted !ascending! lists. new list generated.
    source lists are not changed
    difficulty linear-O(len(a)+len(b))
    :param a: list1
    :param b: list2
    :return: list1 merged with list2 saving ascending order
    """
    res = []
    b_index = 0
    a_index = 0
    while True:
        if int(a[a_index]) < int(b[b_index]):
            res.append(a[a_index])
            a_index += 1
        else:
            res.append(b[b_index])
            b_index += 1

        if b_index == len(b):
            res.extend(a[a_index:])
            break
        if a_index == len(a):
            res.extend(b[b_index:])
            break
    return res


if __name__ == "__main__":
    main()
