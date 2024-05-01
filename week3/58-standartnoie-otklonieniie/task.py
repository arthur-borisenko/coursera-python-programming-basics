import math


def get_list_average(seq: list) -> float:
    elements_sum = 0
    elements_count = 0
    for el in seq:
        elements_count += 1
        elements_sum += el
    res = elements_sum / elements_count
    return res


def get_sequence() -> list:
    seq = []
    while True:
        n = int(input())
        if n == 0:
            break
        seq.append(n)
    return seq


def main():
    deviations_squares_sum = 0
    seq = get_sequence()
    avg = get_list_average(seq)
    for el in seq:
        deviations_squares_sum += (el - avg) ** 2
    result = math.sqrt(deviations_squares_sum / (len(seq) - 1))
    print(result)


if __name__ == '__main__':
    main()
