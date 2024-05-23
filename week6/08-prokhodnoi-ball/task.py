class Student:
    name = ""
    first = 0
    second = 0
    third = 0
    sum = 0


def main():
    with open("input.txt", encoding="utf-8") as input_file, open(
            "output.txt", "w", encoding="utf-8") as output_file:
        k = int(input_file.readline())
        input_lines = input_file.readlines()
        print(get_min_score(input_lines, k), file=output_file)


def count_by_key(input_list, pattern, key=lambda x: x):
    res = 0
    for el in input_list:
        if key(el) == pattern:
            res += 1
    return res


def get_min_score(input_lines, k):
    students = []
    for line in input_lines:
        student = Student()
        temp_student_data = line.split()
        student.third, student.second, student.first = \
            map(int, temp_student_data[-1:-4:-1])
        student.sum = student.third + student.first + student.second
        student.name = " ".join(temp_student_data[:-3])
        if (student.first >= 40 and student.second >= 40 and
                student.third >= 40):
            students.append(student)
    students.sort(key=lambda student: student.sum, reverse=True)
    if len(students) <= k:
        return 0
    if count_by_key(students,
                    max(students, key=lambda el: el.sum).sum,
                    lambda x: x.sum) > k:
        return 1
    else:
        enrollment_score = students[0].sum
        fail_score = students[k].sum
        for i in range(k):
            if students[i].sum > fail_score:
                enrollment_score = students[i].sum
        return enrollment_score


if __name__ == "__main__":
    main()
