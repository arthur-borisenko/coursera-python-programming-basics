# Week 9 - Python Programming Basics

## Overview

This week focuses on sets and dictonaries in Python. Below is a detailed description of each task for Week 7.

### Learning Objectives

* Sorting in python
* Merge and count sort algorithms

## Task Descriptions

### Task 1 - Merge sort algorithm

- **Description:** write merge sort
- **Code Snippet**:

```python
def merge(a, b):
    """
    merge two sorted !ascending! lists. new list generated.
    source lists are not changed
    difficulty linear-O(len(a)+len(b))
    :param a: list1
    :param b: list2
    :return: list1 merged with list2 saving ascending order
    """
    res = []
    b_index = 0
    a_index = 0
    while True:
        if int(a[a_index]) < int(b[b_index]):
            res.append(a[a_index])
            a_index += 1
        else:
            res.append(b[b_index])
            b_index += 1

        if b_index == len(b):
            res.extend(a[a_index:])
            break
        if a_index == len(a):
            res.extend(b[b_index:])
            break
    return res
```

### Task 2 - standard python sort

- **Description**: Use standard sort
- **Code Snippet**:

```python
print(*sorted(input_list))
```

### Task 3 - standard python sort

- **Description**: Use standard sort
- **Code Snippet**:

```python
input_list.sort()
```

### Task 4 - standard sort key parameter, lambda functions

- **Description**: standard sort key parameter, lambda functions
- **Code Snippet**:

```python
village_list.sort(key=lambda i: i[0])
bomb_list.sort(key=lambda i: i[0])
```

### Task 4 - standard sort key parameter, lambda functions practice

- **Description**: standard sort key parameter, lambda functions
- **code snippet**

```python
input_list_without_school_number.sort(key=lambda el: el[0])
```

### Task 6 - count sort

- **Description**: Write count sort algorithm
- **Code Snippet**:

```python
def countSort(input_list):
    cnt_arr = [0] * 101
    for el in input_list:
        cnt_arr[int(el)] += 1
    index = 0
    for i in range(0, 101):
        for j in range(cnt_arr[i]):
            input_list[index] = i
            index += 1
```

### Task 7 - class as structure

- **Description**: Use class as structure
- **Code Snippet**:

```python
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
```

### Task 8 - practice

- **Description**: All week practice
- **Code Snippet**:

```python
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

```
