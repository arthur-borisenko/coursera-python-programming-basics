def main():
    with open("input.txt", encoding="utf-8") as input_file, open(
            "output.txt", "w", encoding="utf-8") as output_file:
        max_n = int(input_file.readline())
        result = set(range(1, max_n + 1))
        question = input_file.readline().split()
        while question != ['HELP']:
            q = set(map(int, question))
            yes_result = result & q
            no_result = result - q
            if len(yes_result) > len(no_result):
                print("YES", file=output_file)
                result = yes_result
            else:
                print("NO", file=output_file)
                result = no_result
            question = input_file.readline().split()
        print(*sorted(result, key=int), file=output_file)


if __name__ == "__main__":
    main()
