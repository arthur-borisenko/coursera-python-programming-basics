def main():
    res = 0
    currentRes = 0
    prevN = InputIntStream().__next__()
    for n in InputIntStream():
        if prevN == n:
            currentRes += 1
        else:
            currentRes = 0
        if currentRes > res:
            res = currentRes
        prevN = n
    print(res + 1)


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
