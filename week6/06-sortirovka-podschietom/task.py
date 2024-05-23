def main():
    input_list = input().split()
    countSort(input_list)
    print(*input_list)


def countSort(input_list):
    cnt_arr = [0] * 101
    for el in input_list:
        cnt_arr[int(el)] += 1
    index = 0
    for i in range(0, 101):
        for j in range(cnt_arr[i]):
            input_list[index] = i
            index += 1


if __name__ == "__main__":
    main()
