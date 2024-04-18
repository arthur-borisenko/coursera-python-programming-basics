def check_is_local_maximum(prev_n, n, post_n):
    return n > prev_n and n > post_n


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


def get_local_maximums_minimal_distance(input_int_stream: InputIntStream):
    result = None
    i = 2
    prev_local_maximum_pos = None
    try:
        prev_prev_n = input_int_stream.__next__()
        prev_n = input_int_stream.__next__()
    except StopIteration:
        return 0
    else:
        for n in input_int_stream:
            if check_is_local_maximum(prev_prev_n, prev_n, n):
                if prev_local_maximum_pos is not None:
                    if (result is None or i -
                            prev_local_maximum_pos - 1 <= result):
                        result = i - prev_local_maximum_pos - 1
                prev_local_maximum_pos = i - 1
            prev_prev_n = prev_n
            prev_n = n
            i += 1
        if result is None:
            return 0
        return result


def main():
    print(get_local_maximums_minimal_distance(InputIntStream()))


if __name__ == '__main__':
    main()
