def korov(number: int) -> str:
    if 11 <= number <= 19:
        return "korov"
    else:
        lastDigit = number % 10
        if lastDigit == 0:
            return "korov"
        elif lastDigit == 1:
            return "korova"
        elif 1 < lastDigit < 5:
            return "korovy"
        elif lastDigit == 11:
            return "korov"
        else:
            return "korov"


def main():
    n = int(input())
    print(n, korov(n))


if __name__ == '__main__':
    main()
