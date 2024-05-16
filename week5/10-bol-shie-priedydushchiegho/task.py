def main():
    input_list = input().split()
    result = []
    prev_n = int(input_list[0])
    input_list = input_list[1:]
    for n in input_list:
        n_int = int(n)
        if n_int > prev_n:
            result.append(n)
        prev_n = n_int
    print(*result)


if __name__ == "__main__":
    main()
