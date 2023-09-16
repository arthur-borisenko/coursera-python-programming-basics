def main():
    sum = find_seqence_sum(InputIntStream())
    print(sum)


def find_seqence_sum(iterator):
    result = 0
    for number in iterator:
        result += number
    return result


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
