def main():
    input_list = input().split(" ")
    res = []
    for el in input_list:
        el_integer = int(el)
        if el_integer % 2 == 0:
            res.append(el_integer)
    print(*res)


if __name__ == "__main__":
    main()
