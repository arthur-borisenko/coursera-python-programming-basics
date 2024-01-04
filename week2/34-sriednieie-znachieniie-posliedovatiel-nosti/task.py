def main():
    ssum = 0
    slen = 0
    while True:
        n = int(input())
        if n == 0:
            break
        slen += 1
        ssum += n
    print(ssum / slen)


if __name__ == '__main__':
    main()
