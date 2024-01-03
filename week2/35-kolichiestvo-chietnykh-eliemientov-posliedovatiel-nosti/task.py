def main():
    count = find_even_numbers_count(InputIntStream())
    print(count)


def find_even_numbers_count(iterator):
    result = 0
    for number in iterator:
        if number % 2 == 0:
            result += 1
    return result


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
