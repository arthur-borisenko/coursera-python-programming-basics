def main():
    n = get_fibonacci_number(int(input()))
    print(n)


def get_fibonacci_number(N):
    Fn2 = 1
    Fn1 = 0
    Fn = 0
    for i in range(N):
        Fn = Fn1 + Fn2
        Fn2 = Fn1
        Fn1 = Fn
    return Fn


if __name__ == '__main__':
    main()
