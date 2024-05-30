# Week 5 - Python Programming Basics

## Overview

This week focuses on for loops, lists and ranges in Python. Below is a detailed description of each task for Week 5.

### Learning Objectives

* for loops
* lists
* ranges

## Task Descriptions

### Task 1 - range as iterable

- **Description**: using range as iterable
- **Code snippet**:
```python
A, B = int(input()), int(input())
print(*range(A, B + 1))
```

### Task 2 - range as iterable

- **Description**: using range as iterable
- **Code snippet**:
```python
A, B = int(input()), int(input())
if A <= B:
    print(*range(A, B + 1))
else:
    print(*range(A, B - 1, -1))
```

### Task 3 - for loops, lists

- **Description**: use for loops and lists
- **Code snippet**

```python
result_lines = ["", "", "", ""]
for i in range(n):
    for j in range(len(FLAG_LINES_TEMPLATE)):
        result_lines[j] += safe_format(FLAG_LINES_TEMPLATE[j],
                                       i + 1)
```

### Task 4 - range as iterable practice

- **Description**: range as iterable practice
- **Code Snippet**:

```python
# task.py
for i in range(1, n + 1):
    print(*range(1, i + 1), sep="")
```

### Task 5 - lists

- **Description** using lists
- **code snippet**

```python
res = []
for n in range(10, 100):
    if (n // 10) * (n % 10) * 2 == n:
        res.append(n)
print(*res)
```

### Task 6 - range with step argument

- **Description**: Use range(start,stop,step) to skip some sequence elements
- **Code Snippet**:

```python
range(0, len(seq), 2)
```

### Task 7 - for loop with lists

- **Description**: Use for loop in lists
- **Code Snippet**:

```python
for el in input_list:
    ...
```

### Task 8 - practice

- **Description**: For loop using practice
- **Code Snippet**:

```python
input_list = input().split(" ")
positive_count = 0
for element in input_list:
    if int(element) > 0:
        positive_count += 1
print(positive_count)
```

### Task 9 - len() function

- **Description**: Use len() function to get list length
- **Code Snippet**:

```python
len(input_list)
```

### Task 10 - list cutting

- **Description:** using cuts with lists
- **Code shippet**

```python
input_list = input_list[1:]
```

### Task 11 - linear search

- **Description:** write linear search algorithm with conditions
- **Code shippet**

```python
input_list = input().split()
minimum = None
for n in input_list:
    n_int = int(n)
    if (minimum is None or n_int < minimum) and n_int > 0:
        minimum = n_int
print(minimum)
```

### Task 12 - abs() function

- **Description:** using abs() to get absolute value of number
- **Code snippet:**

```python
def get_number_distance(a, b):
    return abs(a - b)
```

### Task 13 - for loops and lists practice

- **Description:** for loops and lists practice
- **Code snippet:**

```python
input_list = input().split()
for i in range(0, len(input_list) - 1, 2):
    (input_list[i], input_list[i + 1]) = (
        input_list[i + 1], input_list[i])
print(*input_list)
```

### Task 14 - practice

- **Description:** all week practice
- **Code shippet**

```python
def main():
    input_list = input().split()
    min_i, max_i = get_min_and_max_indexes(input_list)
    (input_list[min_i], input_list[max_i]) = (
        input_list[max_i], input_list[min_i])
    print(*input_list)
    pass


def get_min_and_max_indexes(num_list) -> (
        int, int):
    min_el_index, max_el_index = None, None
    min_el, max_el = None, None
    for i in range(len(num_list)):
        current_num = int(num_list[i])
        if min_el is None or current_num <= min_el:
            min_el = current_num
            min_el_index = i
        if max_el is None or current_num >= max_el:
            max_el = current_num
            max_el_index = i
    return min_el_index, max_el_index
```