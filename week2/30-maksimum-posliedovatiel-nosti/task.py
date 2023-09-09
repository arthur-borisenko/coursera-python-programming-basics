
def main():
    max_number = find_max(InputIntStream())
    print(max_number)


def find_max(iterator):
    max_number = None
    for number in iterator:
        if (max_number is None) or number > max_number:
            max_number = number
    return max_number


class InputIntStream():
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
