INSERT_PATTERN = "*"


def main():
    s = input()
    print(s.replace("", INSERT_PATTERN)[1:-1])


if __name__ == "__main__":
    main()
