def main():
    N = int(input())
    for naturalDivider in range(2, N + 1):
        if N % naturalDivider == 0:
            print(naturalDivider)
            break


if __name__ == '__main__':
    main()
