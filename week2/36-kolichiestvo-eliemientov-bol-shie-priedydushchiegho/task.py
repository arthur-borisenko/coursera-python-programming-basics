def main():
    res = 0
    number = int(input())
    while number != 0:
        prevNumber = number
        number = int(input())
        if number > prevNumber and number != 0:
            res += 1
    print(res)


if __name__ == '__main__':
    main()
