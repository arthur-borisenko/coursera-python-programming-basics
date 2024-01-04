def getSequence() -> list:
    res = []
    i = int(input())
    while i != 0:
        res.append(i)
        i = int(input())
    return res


def main():
    seq = getSequence()
    res = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[i - 1]:
            res += 1
    print(res)


if __name__ == '__main__':
    main()
