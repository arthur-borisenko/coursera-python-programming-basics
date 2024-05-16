def main():
    input_list = input().split(" ")
    max_number = int(input_list[0])
    max_last_index = 0
    for i in range(len(input_list)):
        number = int(input_list[i])
        if number >= max_number:
            max_number = number
            max_last_index = i
    print(max_number, max_last_index)


if __name__ == "__main__":
    main()
