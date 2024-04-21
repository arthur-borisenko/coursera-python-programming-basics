def main():
    elements_sum = 0
    elements_count = 0
    input_int_stream = InputIntStream()
    for el in input_int_stream:
        elements_count += 1
        elements_sum += el
    res = elements_sum / elements_count
    symb_arter_colon = 12 - len(str(int(res // 1)))
    res = res.__round__(symb_arter_colon)
    print(res)


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
