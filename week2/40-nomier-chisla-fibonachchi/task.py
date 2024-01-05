def main():
    required_Fn = int(input())
    n = get_n_by_fibonacci_number(required_Fn)
    print(n)


def get_n_by_fibonacci_number(required_Fn):
    Fn2 = 1
    Fn1 = 0
    n = 0
    while True:
        n += 1
        Fn = Fn1 + Fn2
        Fn2 = Fn1
        Fn1 = Fn
        if Fn == required_Fn:
            return n
        if Fn > required_Fn:
            return -1


if __name__ == '__main__':
    main()
