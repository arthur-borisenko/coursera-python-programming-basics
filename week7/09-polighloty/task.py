def main():
    all_students_know_set = None
    at_least_one_student_know_set = set()
    n = int(input())
    for i in range(n):
        current_student_know_set = set()
        m = int(input())
        for j in range(m):
            current_student_know_set.add(input().strip())
        at_least_one_student_know_set |= current_student_know_set
        if all_students_know_set is None:
            all_students_know_set = current_student_know_set
        else:
            all_students_know_set = all_students_know_set \
                                    & current_student_know_set
    print(len(all_students_know_set))
    print(*all_students_know_set, sep="\n")
    print(len(at_least_one_student_know_set))
    print(*at_least_one_student_know_set, sep="\n")


if __name__ == "__main__":
    main()
