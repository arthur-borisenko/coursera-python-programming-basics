def main():
    s = input()
    print(count_words(s))


def count_words(s):
    return s.count(" ") + 1


if __name__ == "__main__":
    main()
