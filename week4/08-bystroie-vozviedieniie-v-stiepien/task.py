def main():
    base, exponent = float(input()), int(input())
    print(power(base, exponent))


def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        return power(base * base, exponent / 2)
    else:
        return base * power(base, exponent - 1)


if __name__ == "__main__":
    main()
