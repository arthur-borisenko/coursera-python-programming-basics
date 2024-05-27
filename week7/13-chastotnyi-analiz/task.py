def main():
    with open("input.txt", encoding="utf-8") as input_file, open(
            "output.txt", "w", encoding="utf-8") as output_file:
        words = input_file.read().split()
        words_dict = {}
        for word in words:
            words_dict[word] = words_dict.get(word, 0) + 1
        print(*map(lambda el: el[0], sorted(words_dict.items(),
                                            key=lambda el: (
                                                -el[1], el[0]))),
              file=output_file, sep="\n")


if __name__ == "__main__":
    main()
