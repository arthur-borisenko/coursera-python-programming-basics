def maximumNumber(listNums: list):
    maxCurrentNum = 0
    for el in listNums:
        if el > maxCurrentNum:
            maxCurrentNum = el
    return maxCurrentNum


def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    all1 = [n1, n2, n3]
    print(max(all1))


if __name__ == '__main__':
    main()
