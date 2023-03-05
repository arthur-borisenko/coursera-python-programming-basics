def main():
    A, B, N = int(input()), int(input()), int(input())
    rubles = A * N
    pennies = B * N
    result_rubles = rubles + pennies // 100
    result_pennies = pennies % 100
    print(result_rubles, result_pennies)


if __name__ == '__main__':
    main()
