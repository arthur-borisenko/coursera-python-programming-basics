def main():
    s = input()
    first = s.find("f")
    last = len(s) - s[::-1].find("f") - 1
    if first != -1:
        if first == last:
            print(first)
        else:
            print(first, last)


if __name__ == '__main__':
    main()
