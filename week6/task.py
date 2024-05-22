def main():
    print(*merge(input().split(), input().split()))
    pass


def merge(a, b):
    res = []
    if a[0] > b[0]:
        a1, b1 = b, a
    else:
        a1, b1 = a, b

    if len(a1) == 0:
        return b1
    elif len(a1) == 1:
        for b_index in range(len(b1)):
            res.append(b1[b_index])
            if a1[0] >= b1[b_index]:
                res.append(a1[0])
    else:
        b_index = 0
        for a_index in range(len(a1) - 1):
            res.append(a1[a_index])
            while b_index < len(b1) and b1[b_index] <= a1[
                    a_index + 1]:
                res.append(b1[b_index])
                b_index += 1
        res.append(a1[-1])
        res.extend(b1[b_index + 1:])
    return res


if __name__ == "__main__":
    main()
