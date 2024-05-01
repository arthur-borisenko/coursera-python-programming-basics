def percents_per_year(percents, rubles, kopecks):
    input_in_kopecks = 100 * rubles + kopecks
    percent_sum = 100 + percents
    result_in_kopecks = input_in_kopecks * percent_sum / 100
    result_rubles = int(result_in_kopecks // 100)
    result_kopecks = int(result_in_kopecks % 100)
    return result_rubles, result_kopecks


def main():
    P, X, Y, K = int(input()), int(input()), int(input()), int(input())
    for i in range(K):
        X, Y = percents_per_year(P, X, Y)
    print(X, Y)


if __name__ == '__main__':
    main()
