def main():
    a, b, c, d, e = int(input()), int(input()), \
        int(input()), int(input()), int(input())
    if a > b:
        (a, b) = (b, a)
    if b > c:
        (b, c) = (c, b)
        if a > b:
            (a, b) = (b, a)
    if d > e:
        (d, e) = (e, d)
    if d >= a and e >= b:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
