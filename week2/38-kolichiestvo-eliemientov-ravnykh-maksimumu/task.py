def count_max_elements(seq):
    max_numbers_count = 0
    max_el = None
    for el in seq:
        if max_el is None or max_el < el:
            max_numbers_count = 0
            max_el = el
        if el == max_el:
            max_numbers_count += 1
    return max_numbers_count


def main():
    seq = InputIntStream()
    print(count_max_elements(seq))


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
