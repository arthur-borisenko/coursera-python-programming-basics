def main():
    n1 = input()
    n2 = input()
    t1 = int(n1) % int(n2) == 0
    t2 = t1 * 1
    t3 = (t2 + 1) % 2
    print(t2 * "YES", t3 * "NO", sep="")


if __name__ == '__main__':
    main()
