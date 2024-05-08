def main():
    s = input()
    first = s.find("h")
    last = len(s) - s[::-1].find("h") - 1
    print(s[:first] + s[last + 1:])


if __name__ == '__main__':
    main()
