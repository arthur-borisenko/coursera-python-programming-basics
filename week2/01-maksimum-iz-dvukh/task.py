def maximumNumber(listNums: list):
    maxCurrentNum = 0
    for el in listNums:
        if el > maxCurrentNum:
            maxCurrentNum = el
    return maxCurrentNum


def main():
    number1 = int(input())
    number2 = int(input())
    print(maximumNumber([number1, number2]))


if __name__ == '__main__':
    main()
