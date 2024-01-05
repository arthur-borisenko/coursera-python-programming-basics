def main():
    prev2N = 1
    prevN = 0
    n = 0
    for i in range(int(input())):
        n = prevN + prev2N
        prev2N = prevN
        prevN = n
    print(n)


if __name__ == '__main__':
    main()
