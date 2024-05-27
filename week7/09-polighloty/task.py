def main():
    with (open("input.txt", encoding="utf-8") as input_file, open(
            "output.txt", "w", encoding="utf-8") as output_file):
        all_students_know_set = None
        at_least_one_student_know_set = set()
        n = int(input_file.readline())
        for i in range(n):
            current_student_know_set = set()
            m = int(input_file.readline())
            for j in range(m):
                current_student_know_set.add(input_file.readline().strip())
            at_least_one_student_know_set |= current_student_know_set
            if all_students_know_set is None:
                all_students_know_set = current_student_know_set
            else:
                all_students_know_set = all_students_know_set \
                                        & current_student_know_set
        print(len(all_students_know_set), file=output_file)
        print(*all_students_know_set, sep="\n", file=output_file)
        print(len(at_least_one_student_know_set), file=output_file)
        print(*at_least_one_student_know_set, sep="\n",
              file=output_file)


if __name__ == "__main__":
    main()
