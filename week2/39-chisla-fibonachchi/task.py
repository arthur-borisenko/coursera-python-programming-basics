def main():
    n = int(input())
    Fn = get_fibonacci_number(n)
    print(Fn)


def get_fibonacci_number(n):
    Fn2 = 1
    Fn1 = 0
    Fn = 0
    for i in range(n):
        Fn = Fn1 + Fn2
        Fn2 = Fn1
        Fn1 = Fn
    return Fn


if __name__ == '__main__':
    main()
