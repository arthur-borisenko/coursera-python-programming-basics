def main():
    n, x = int(input()), float(input())
    res = calc_gornier_scheme(n, x,
                              SimpleInputFloatStream(n + 1))
    if res.is_integer():
        print(int(res))
    else:
        print(res)


class SimpleInputFloatStream:
    i = 0
    count = 1

    def __len__(self):
        return self.count

    def __init__(self, count: int):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        self.current = float(input())
        if self.i < self.count:
            self.i += 1
            return self.current
        raise StopIteration


def calc_gornier_scheme(n, x, stream):
    prev_part = 0
    for i in range(n):
        a = stream.__next__()
        prev_part = (prev_part + a) * x
    prev_part += stream.__next__()
    return prev_part


if __name__ == '__main__':
    main()
