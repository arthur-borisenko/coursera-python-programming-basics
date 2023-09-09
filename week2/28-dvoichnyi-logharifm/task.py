def main():
    N = int(input())
    currentPower = 0
    while power(2, currentPower) < N:
        currentPower += 1
    print(currentPower)


def power(n: int, p: int) -> int:
    result = 1
    for i in range(p):
        result *= n
    return result


if __name__ == '__main__':
    main()
