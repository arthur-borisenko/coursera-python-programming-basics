def main():
    k = int(input())
    result = "NO"
    for x in range(0, k):
        if (k - 3 * x) % 5 == 0 and (k - 3 * x) >= 0:
            result = "YES"
    print(result)
    pass


if __name__ == '__main__':
    main()
