def main():
    with open("input.txt", encoding="utf-8") as input_file, open(
            "output.txt", "w", encoding="utf-8") as output_file:
        input_list = input_file.readlines()
        input_list_without_school_number = []
        for line in input_list:
            last_name, first_name, school_number, points = line.split()
            input_list_without_school_number.append(
                [last_name, first_name, points])
        input_list_without_school_number.sort(key=lambda el: el[0])
        for line in input_list_without_school_number:
            print(*line, file=output_file)


if __name__ == "__main__":
    main()
