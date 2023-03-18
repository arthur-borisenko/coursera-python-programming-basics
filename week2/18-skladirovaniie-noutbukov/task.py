def main():
    dd, ee, ff, aa, bb, cc = int(input()), int(input()), \
        int(input()), int(input()), int(input()), int(input()),

    def findBoxNumber(a, b, c, a1, b1, c1):
        return (a1 // a) * (b1 // b) * (c1 // c)

    n1 = findBoxNumber(aa, bb, cc, dd, ee, ff)
    n2 = findBoxNumber(aa, bb, cc, ee, dd, ff)
    n3 = findBoxNumber(aa, bb, cc, ff, dd, ee)
    n4 = findBoxNumber(aa, bb, cc, dd, ff, ee)
    n5 = findBoxNumber(aa, bb, cc, ee, ff, dd)
    n6 = findBoxNumber(aa, bb, cc, ff, ee, dd)
    print(max(n1, n2, n3, n4, n5, n6))


if __name__ == '__main__':
    main()
