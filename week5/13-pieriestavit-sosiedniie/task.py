def main():
    input_list = input().split()
    for i in range(0, len(input_list)-1, 2):
        (input_list[i], input_list[i + 1]) = (
            input_list[i + 1], input_list[i])
    print(*input_list)


if __name__ == "__main__":
    main()
