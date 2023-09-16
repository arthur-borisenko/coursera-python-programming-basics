def main():
    n = int(input())
    result = 0
    for i in range(n):
        result += (i + 1) ** 2
    print(result)


if __name__ == '__main__':
    main()
