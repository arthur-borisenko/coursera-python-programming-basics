def main():
    s = input()
    first = s.find("f")
    if first == -1:
        print(-2)
    else:
        if s[first + 1:].find("f") != -1:
            print(s[first + 1:].find("f") + len(s[:first + 1]))
        else:
            print(-1)


if __name__ == '__main__':
    main()
