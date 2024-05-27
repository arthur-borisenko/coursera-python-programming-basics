def main():
    with open("input.txt", "r") as input_file, open("output.txt",
                                                    "w") as output_file:
        words = input_file.read().split()
        words_count_dict = {}
        for word in words:
            words_count_dict[word] = words_count_dict.get(word,
                                                          0) + 1
        print(
            min(words_count_dict.items(),
                key=lambda el: (-el[1], el[0]))[0], file=output_file)


if __name__ == "__main__":
    main()
