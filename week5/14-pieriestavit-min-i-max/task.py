def main():
    input_list = input().split()
    min_i, max_i = get_min_and_max_indexes(input_list)
    (input_list[min_i], input_list[max_i]) = (
        input_list[max_i], input_list[min_i])
    print(*input_list)
    pass


def get_min_and_max_indexes(num_list) -> (
        int, int):
    min_el, max_el, min_el_index, max_el_index = num_list[0], \
        num_list[0], 0, 0
    for i in range(len(num_list)):
        if num_list[i] < min_el:
            min_el = num_list[i]
            min_el_index = i
        if num_list[i] > max_el:
            max_el = num_list[i]
            max_el_index = i
    return min_el_index, max_el_index


if __name__ == "__main__":
    main()
