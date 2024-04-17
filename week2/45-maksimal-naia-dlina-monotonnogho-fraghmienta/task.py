def main():
    res = count_max_()
    print(res + 1)


def count_max_():
    res = 0
    currentRes = 0
    # 0 - больше предыдущего, 1 - меньше
    currentFragmentType = None
    prevFragmentType = None
    iterator = InputIntStream()
    prevN = iterator.__next__()
    for n in iterator:
        if prevN < n:
            currentFragmentType = 0
        elif prevN > n:
            currentFragmentType = 1
        else:
            currentFragmentType = None
        prevN = n
        if (prevFragmentType == currentFragmentType and
                currentFragmentType is not None):
            currentRes += 1
        else:
            if currentFragmentType is not None:
                currentRes = 1
            else:
                currentRes = 0
        if currentRes > res:
            res = currentRes
        prevFragmentType = currentFragmentType
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
