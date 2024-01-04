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
    prevNumber = None
    for number in iterator:
        if prevNumber is None:
            prevNumber = number
        else:
            if number > prevNumber and number != 0:
                res += 1
            prevNumber = number
    print(res)


if __name__ == '__main__':
    main()
