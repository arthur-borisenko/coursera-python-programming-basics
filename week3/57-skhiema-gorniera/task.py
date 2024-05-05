def safe_to_int(n):
    if hasattr(n, "is_integer") and n.is_integer():
        return int(n)
    else:
        return n


def main():
    n, x = int(input()), float(input())
    res = calc_gornier_scheme(x, BoundedFloatInputStream(n + 1))
    print(safe_to_int(res))


class BoundedFloatInputStream:
    size = 0
    max_size = 0

    def __iter__(self):
        return self

    def __init__(self, max_size: int):
        self.max_size = max_size

    def __next__(self):
        if self.size < self.max_size:
            self.current = float(input())
            self.size += 1
            return self.current
        raise StopIteration


def calc_gornier_scheme(x, stream):
    a_n = stream.__next__()
    for a_n_minus_1 in stream:
        a_n = a_n * x + a_n_minus_1
    return a_n


if __name__ == '__main__':
    main()
