def main():
    input_list = input().split()
    minimum = None
    for n in input_list:
        n_int = int(n)
        if (minimum is None or n_int < minimum) and n_int > 0:
            minimum = n_int
    print(minimum)


if __name__ == "__main__":
    main()
