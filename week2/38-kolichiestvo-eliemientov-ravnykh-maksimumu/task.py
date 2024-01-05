def count_maximum_elements(seq):
    res = 0
    max_el = None
    for el in seq:
        if max_el is None or max_el < el:
            res = 0
            max_el = el
        if el == max_el:
            res += 1
    return res


def main():
    seq = InputIntStream()
    print(count_maximum_elements(seq))


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
