class Student:
    fullName = ""
    firstScore = 0
    secondScore = 0
    thirdScore = 0
    total = 0


def main():
    with open("input.txt", encoding="utf-8") as input_file, open(
            "output.txt", "w", encoding="utf-8") as output_file:
        k = int(input_file.readline())
        input_lines = input_file.readlines()
        students = []
        for line in input_lines:
            student = parse_student(line)
            students.append(student)

        print(find_enrollment_score(students, k), file=output_file)


def find_enrollment_score(students, k):
    students = list(
        filter(lambda el: check_min_requirements(el), students))
    students.sort(key=lambda el: el.total, reverse=True)

    if len(students) <= k:
        return 0

    max_total = max(students, key=lambda el: el.total).total
    count_max_total = count(students,
                            key=lambda el: el.total == max_total)
    if count_max_total > k:
        return 1

    return find_min_total_greater_then(students, students[k].total)


def find_min_total_greater_then(students, fail_total):
    enrollment_score = None
    for i in range(len(students)):
        if (enrollment_score is None or
                fail_total < students[
                    i].total < enrollment_score):
            enrollment_score = students[i].total
    return enrollment_score


def parse_student(line):
    student = Student()
    words = line.split()
    student.thirdScore, student.secondScore, student.firstScore = \
        int(words[-1]), int(words[-2]), int(words[-3])
    student.total = (student.thirdScore +
                     student.firstScore + student.secondScore)
    student.fullName = " ".join(words[:-4])
    return student


def check_min_requirements(student):
    return not (student.firstScore < 40 or
                student.secondScore < 40 or
                student.thirdScore < 40)


def count(input_list, key=lambda x: True):
    res = 0
    for el in input_list:
        if key(el):
            res += 1
    return res


if __name__ == "__main__":
    main()
