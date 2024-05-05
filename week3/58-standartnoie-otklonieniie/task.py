import math


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
    input_stream = InputIntStream()
    elements_sum = 0
    elements_count = 0
    elements_squares_sum = 0
    for el in input_stream:
        elements_count += 1
        elements_sum += el
        elements_squares_sum += el ** 2
    average = elements_sum / elements_count
    result = math.sqrt((elements_squares_sum -
                        2 * average * elements_sum +
                        elements_count * average ** 2) /
                       (elements_count - 1))
    print(result)


if __name__ == '__main__':
    main()
