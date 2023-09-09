def main():
    N = int(input())
    result = []
    currentPower = 0
    while power(2, currentPower) <= N:
        result.append(str(power(2, currentPower)))
        currentPower += 1
    print(" ".join(result))


def power(n: int, p: int) -> int:
    result = 1
    for i in range(p):
        result *= n
    return result


if __name__ == '__main__':
    main()
