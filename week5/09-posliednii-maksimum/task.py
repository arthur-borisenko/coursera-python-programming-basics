def main():
    input_list = input().split(" ")
    print(*get_last_maximum(input_list))


def safe_to_int(n):
    if hasattr(n, "is_integer") and n.is_integer():
        return int(n)
    else:
        return n


def get_last_maximum(input_list):
    if input_list[0] == "":
        return []
    max_number = float(input_list[0])
    max_last_index = 0
    for i in range(len(input_list)):
        number = float(input_list[i])
        if number >= max_number:
            max_number = number
            max_last_index = i
    return safe_to_int(max_number), max_last_index


if __name__ == "__main__":
    main()
