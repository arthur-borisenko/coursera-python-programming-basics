def maximumNumber(listNums: list):
    maxCurrentNum = 0
    for el in listNums:
        if el > maxCurrentNum:
            maxCurrentNum = el
    return maxCurrentNum


def get0or1or2(maximum: int, all1: list):
    if all1[0] == all1[1]:
        return 0
    elif all1[0] == maximum:
        return 1
    else:
        return 2


def main():
    n0 = int(input())
    n1 = int(input())
    all2 = [n0, n1]
    maximal = max(all2)
    nullOrOneOrTwo = get0or1or2(maximal, all2)
    print(nullOrOneOrTwo)


if __name__ == '__main__':
    main()
