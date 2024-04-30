def main():
    P, X, Y = int(input()), int(input()), int(input())
    input_in_kopecks = 100 * X + Y
    percent_sum = 100 + P
    result_in_kopecks = input_in_kopecks * percent_sum / 100
    result_rubles = int(result_in_kopecks // 100)
    result_kopecks = int(result_in_kopecks % 100)
    print(result_rubles, result_kopecks)


if __name__ == '__main__':
    main()
