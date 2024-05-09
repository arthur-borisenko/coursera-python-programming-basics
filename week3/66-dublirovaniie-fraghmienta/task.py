def main():
    s = input()
    first = s.find("h")
    last = len(s) - s[::-1].find("h") - 1
    print(s[:first + 1] + s[first + 1:last] * 2 + s[last:])


if __name__ == '__main__':
    main()
