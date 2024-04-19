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


# lmax - here is local maximum
def get_lmax_min_dist(input_int_stream: InputIntStream):
    min_lmax_dist = None
    prev_lmax_pos = None
    try:
        prev_prev_n = input_int_stream.__next__()
        prev_n = input_int_stream.__next__()
    except StopIteration:
        return 0
    else:
        for (i, n) in enumerate(input_int_stream):
            if check_is_lmax(prev_prev_n, prev_n, n):
                lmax_pos = i - 1
                lmax_dist = get_lmax_dist(prev_lmax_pos, lmax_pos)
                min_lmax_dist = safe_min(lmax_dist, min_lmax_dist)
                prev_lmax_pos = lmax_pos
            prev_prev_n = prev_n
            prev_n = n
        if min_lmax_dist is None:
            return 0
        return min_lmax_dist


def get_lmax_dist(prev_lmax_pos, lmax_pos):
    lmax_dist = None
    if prev_lmax_pos is not None:
        lmax_dist = lmax_pos - prev_lmax_pos
    return lmax_dist


def check_is_lmax(prev_n, n, post_n):
    return n > prev_n and n > post_n


def safe_min(x, y):
    if y is None or x <= y:
        y = x
    return y


def main():
    print(get_lmax_min_dist(InputIntStream()))


if __name__ == '__main__':
    main()
