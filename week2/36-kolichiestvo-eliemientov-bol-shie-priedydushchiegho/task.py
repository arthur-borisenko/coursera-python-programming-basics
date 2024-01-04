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


def main():
    iterator = InputIntStream()
    res = 0
    prevNumber = next(iterator)
    for number in iterator:
        if number > prevNumber:
            res += 1
        prevNumber = number
    print(res)


if __name__ == '__main__':
    main()
