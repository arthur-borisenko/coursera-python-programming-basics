def main():
    with open("input.txt", encoding="utf-8") as input_file, open(
            "output.txt", "w", encoding="utf-8") as output_file:
        print(len(set(input_file.read().split())), file=output_file)
        pass


if __name__ == "__main__":
    main()
