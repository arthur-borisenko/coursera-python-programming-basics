def main():
    latestPower = 0
    N = int(input())
    currentPower = 0
    while power(2, currentPower) <= N:
        latestPower = power(2, currentPower)
        currentPower += 1
    if latestPower == N:
        print("YES")
    else:
        print("NO")


def power(n: int, p: int) -> int:
    result = 1
    for i in range(p):
        result *= n
    return result


if __name__ == '__main__':
    main()
