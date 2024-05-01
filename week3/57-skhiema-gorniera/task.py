def main():
    n, x = int(input()), float(input())
    prev_part = 0
    for i in range(n):
        a = float(input())
        prev_part = (prev_part + a) * x
    prev_part += float(input())
    if prev_part.is_integer():
        print(int(prev_part))
    else:
        print(prev_part)


if __name__ == '__main__':
    main()
