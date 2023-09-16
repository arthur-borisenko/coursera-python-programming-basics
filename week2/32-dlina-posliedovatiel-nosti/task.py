def main():
    result = 0
    currentNumber = int(input())
    while currentNumber != 0:
        result += 1
        currentNumber = int(input())
    print(result)


if __name__ == '__main__':
    main()
