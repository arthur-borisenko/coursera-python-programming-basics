def main():
    res = count_max_equal_number()
    print(res + 1)


def count_max_equal_number():
    res = 0
    currentRes = 0
    iterator = InputIntStream()
    prevN = iterator.__next__()
    for n in iterator:
        if prevN == n:
            currentRes += 1
        else:
            currentRes = 0
        if currentRes > res:
            res = currentRes
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
