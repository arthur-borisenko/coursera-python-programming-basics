def main():
    N = int(input())
    result = []
    naturalNum = 1
    while naturalNum * naturalNum <= N:
        result.append(str(naturalNum * naturalNum))
        naturalNum += 1
    print(" ".join(result))


if __name__ == '__main__':
    main()
