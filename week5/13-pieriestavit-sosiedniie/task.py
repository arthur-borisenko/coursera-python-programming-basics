def main():
    input_list = input().split()
    last_el = None
    if len(input_list) % 2 != 0:
        last_el = int(input_list[-1])
        del input_list[-1]
    for i in range(0, len(input_list), 2):
        (input_list[i], input_list[i + 1]) = (
            input_list[i + 1], input_list[i])
    if last_el is not None:
        input_list.append(last_el)
    print(*input_list)


if __name__ == "__main__":
    main()
