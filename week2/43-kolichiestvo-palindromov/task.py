def checkPalindrome(string: str) -> int:
    length = len(string)
    result = True
    for i in range(int((length - length % 2) / 2)):
        if not string[i] == string[length - 1 - i]:
            result = False
    return result


def main():
    num = int(input())
    res = 0
    for i in range(1, num + 1):
        if checkPalindrome(str(i)):
            res += 1
    print(res)


if __name__ == '__main__':
    main()
