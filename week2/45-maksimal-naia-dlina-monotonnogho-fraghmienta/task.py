def main():
    res = count_max_()
    print(res)


class pairTypes():
    GROWING = 1
    DESCING = 2


def count_max_():
    res = 1
    currentRes = 2
    prevPairType = None
    iterator = InputIntStream()
    prevN = iterator.__next__()
    for n in iterator:
        if n > prevN:
            currentPairType = pairTypes.GROWING
        elif n < prevN:
            currentPairType = pairTypes.DESCING
        else:
            currentRes = 1
            prevN = n
            continue
        if prevPairType == currentPairType:
            currentRes += 1
        else:
            currentRes = 2
        if currentRes > res:
            res = currentRes
        prevPairType = currentPairType
        prevN = n
    return res


class InputIntStream:
    def __init__(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        self.current = int(input())
        if self.current != 0:
            return self.current
        raise StopIteration


if __name__ == '__main__':
    main()
