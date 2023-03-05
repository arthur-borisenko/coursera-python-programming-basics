def main():
    number = input()
    while len(number) < 4:
        number = "0" + number
    if len(number) % 2 == 1:
        number = number[0: int((len(number)-1) / 2):] +\
                 number[int((len(number)-1) / 2)::]
    for index in range(int(len(number) / 2)):
        if number[index] != number[(-1) - index]:
            print(0)
            return
    print(1)


if __name__ == '__main__':
    main()
