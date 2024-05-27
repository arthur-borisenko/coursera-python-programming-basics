def main():
    with open("input.txt", encoding="utf-8") as input_file, open(
            "output.txt", "w", encoding="utf-8") as output_file:
        before_dict = {}
        res = []
        for word in input_file.read().split():
            res.append(before_dict.get(word, 0))
            before_dict[word] = before_dict.get(word, 0) + 1
        print(*res, file=output_file)


if __name__ == "__main__":
    main()
