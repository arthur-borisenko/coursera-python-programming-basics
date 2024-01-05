def main():
    required_Fn = int(input())
    Fn = get_fibonacci_number_number(required_Fn)
    print(Fn)


def get_fibonacci_number_number(required_Fn):
    Fn2 = 1
    Fn1 = 0
    Fn = 0
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
