def main():
    input_list = input().split(" ")
    res = []
    for el in input_list:
        el = int(el)
        if el % 2 == 0:
            res.append(el)
    print(*res)


if __name__ == "__main__":
    main()
