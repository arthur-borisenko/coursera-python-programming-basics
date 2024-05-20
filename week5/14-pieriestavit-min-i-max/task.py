def main():
    input_list = input().split()
    min_i, max_i = get_min_and_max_indexes(input_list)
    (input_list[min_i], input_list[max_i]) = (
        input_list[max_i], input_list[min_i])
    print(*input_list)
    pass


def get_min_and_max_indexes(num_list) -> (
        int, int):
    min_el_index, max_el_index = None, None
    min_el, max_el = None, None
    for i in range(len(num_list)):
        current_num = int(num_list[i])
        if min_el is None or current_num <= min_el:
            min_el = current_num
            min_el_index = i
        if max_el is None or current_num >= max_el:
            max_el = current_num
            max_el_index = i
    return min_el_index, max_el_index


if __name__ == "__main__":
    main()
