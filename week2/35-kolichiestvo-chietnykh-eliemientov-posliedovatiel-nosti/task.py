def main():
    summa = find_chiethnyh_number(InputIntStream())
    print(summa)


def find_chiethnyh_number(iterator):
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
