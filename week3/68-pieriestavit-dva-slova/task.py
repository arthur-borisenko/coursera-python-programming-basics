def main():
    s = input()
    sep_index = s.find(" ")
    first_word = s[:sep_index]
    second_word = s[sep_index + 1:]
    print(second_word, first_word)


if __name__ == '__main__':
    main()
