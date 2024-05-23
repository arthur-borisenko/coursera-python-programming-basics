class Student:
    full_name = ""
    score = 0


def main():
    n = int(input())
    student_list = []
    for i in range(n):
        student = Student()
        temp_student_data = input().split(" ")
        student.full_name = temp_student_data[0]
        student.score = int(temp_student_data[1])
        student_list.append(student)
    student_list.sort(key=lambda student: student.score, reverse=True)
    for student in student_list:
        print(student.full_name)


if __name__ == "__main__":
    main()
