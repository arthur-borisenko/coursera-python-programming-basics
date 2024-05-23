def main():
    s, n = map(int, input().split())
    input_list = []
    for _ in range(n):
        input_list.append(int(input()))
    input_list.sort()
    spentSize = 0
    i = 0
    while i < len(input_list):
        spentSize += input_list[i]
        if spentSize > s:
            break
        i += 1
    print(i)


if __name__ == "__main__":
    main()
