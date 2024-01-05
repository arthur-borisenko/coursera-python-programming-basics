def main():
    seq = InputIntStream()
    res = get_top_2_element(seq)
    print(res)


def get_top_2_element(seq):
    top_2_el = None
    max_el = None
    for el in seq:
        if max_el is None or max_el <= el:
            top_2_el = max_el
            max_el = el
        elif top_2_el is None or el >= top_2_el:
            top_2_el = el
    return top_2_el


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
