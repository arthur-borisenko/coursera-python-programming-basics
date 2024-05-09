TO_PATTERN = "one"
FROM_PATTERN = "1"


def main():
    s = input()
    print(s.replace(FROM_PATTERN, TO_PATTERN))


if __name__ == "__main__":
    main()
