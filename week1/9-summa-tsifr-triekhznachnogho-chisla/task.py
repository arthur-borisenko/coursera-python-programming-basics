def main():
    n = int(input())
    hundreds = (n // 100)
    tens = (n // 10) - hundreds * 10
    units = n % 10
    print(hundreds + tens + units)


if __name__ == '__main__':
    main()
