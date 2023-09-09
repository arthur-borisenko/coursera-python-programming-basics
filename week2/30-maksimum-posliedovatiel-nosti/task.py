def main():
    inputList = deserialize()
    maxNumber = 0
    for number in inputList:
        if number > maxNumber:
            maxNumber = number
    print(maxNumber)


def deserialize() -> list:
    inputList = []
    recentInput = int(input())
    while recentInput != 0:
        inputList.append(recentInput)
        recentInput = int(input())
    return inputList


if __name__ == '__main__':
    main()
