import math


def main():
    n = float(input())
    n_first_digit_after_colon = int(n * 10) % 10
    if n_first_digit_after_colon >= 5:
        print(math.ceil(n))
    else:
        print(math.floor(n))


if __name__ == '__main__':
    main()
