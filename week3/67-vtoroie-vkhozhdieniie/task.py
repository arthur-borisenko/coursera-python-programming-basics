def main():
    PATTERN = "f"
    s = input()
    first = s.find(PATTERN)
    if first == -1:
        print(-2)
    else:
        if s[first + 1:].find(PATTERN) != -1:
            print(s[first + 1:].find(PATTERN) + len(s[:first + 1]))
        else:
            print(-1)


if __name__ == '__main__':
    main()
