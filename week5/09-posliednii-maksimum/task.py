def main():
    input_list = input().split()
    print(*get_last_maximum(input_list))


def get_last_maximum(input_list):
    max_last_index = 0
    max_number = int(input_list[max_last_index])

    for i in range(len(input_list)):
        number = int(input_list[i])
        if number >= max_number:
            max_number = number
            max_last_index = i
    return max_number, max_last_index


if __name__ == "__main__":
    main()
