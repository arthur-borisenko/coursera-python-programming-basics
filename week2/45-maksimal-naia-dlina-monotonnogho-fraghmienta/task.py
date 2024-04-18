def main():
    res = count_max()
    print(res)


class PairTypes:
    GROWING = 1
    DESC = 2
    EQ = 3


def count_max():
    iterator = InputIntStream()
    max_pairs = 0
    pairs = 0
    prev_pair_type = None
    prev_n = iterator.__next__()
    for n in iterator:
        pair_type = get_pair_type(n, prev_n)
        if pair_type == PairTypes.EQ or pair_type is None:
            pairs = 0
        elif prev_pair_type != pair_type:
            pairs = 1
        else:
            pairs += 1

        if pairs > max_pairs:
            max_pairs = pairs

        prev_pair_type = pair_type
        prev_n = n

    return count_elements_in_pairs(max_pairs)


def count_elements_in_pairs(max_pairs):
    return max_pairs + 1


def get_pair_type(n, prev_n):
    if n > prev_n:
        pair_type = PairTypes.GROWING
    elif n < prev_n:
        pair_type = PairTypes.DESC
    else:
        pair_type = PairTypes.EQ
    return pair_type


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
