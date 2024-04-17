def check_is_local_maximum(prev_n, n, post_n):
    return n > prev_n and n > post_n


def get_input_int_sequence():
    r = []
    while True:
        n = int(input())
        if n != 0:
            r.append(n)
        else:
            return r


def get_local_maximums_positions_list(input_sequence):
    result = []
    if len(input_sequence) < 2:
        return []
    prev_prev_n = input_sequence[0]
    prev_n = input_sequence[1]
    for i in range(2, len(input_sequence)):
        n = input_sequence[i]
        if check_is_local_maximum(prev_prev_n, prev_n, n):
            result.append(i - 1)
        prev_prev_n = prev_n
        prev_n = n
        i += 1
    return result


def main():
    input_list = get_input_int_sequence()
    local_maximums_positions_list = \
        get_local_maximums_positions_list(input_list)
    if len(local_maximums_positions_list) < 2:
        print("0")
    else:
        res = None
        for index in range(1, len(local_maximums_positions_list)):
            if res is None or (local_maximums_positions_list[index] -
                               local_maximums_positions_list[index - 1] < res):
                res = (local_maximums_positions_list[index] -
                       local_maximums_positions_list[index - 1])
        print(res)


if __name__ == '__main__':
    main()
