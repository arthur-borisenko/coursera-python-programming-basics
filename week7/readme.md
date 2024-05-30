# Week 7 - Python Programming Basics

## Overview

This week focuses on sets and dictonaries in Python. Below is a detailed description of each task for Week 7.

### Learning Objectives

* Sets and dictionaries in python
* Class as structure

## Task Descriptions

### Task 1 - Sets in python

- **Description**:
- Basic set principles
- creating sets
- **Code Snippet**:

```python
print(
    len(
        set(
            input()
            .split()
        )
    )
)
```

### Task 2 - sets intersect

- **Description**: Use sets intersect
- **Code Snippet**:

```python
print(
    len(
        set(
            input()
            .split()
        )
        &
        set(
            input()
            .split()
        )
    )
)
```

### Task 3 - sets intersect

- **Description**: Use sets intersect
- **Code Snippet**:

```python
print(
    *sorted(
        set(
            map(
                int,
                input()
                .split()
            )
        )
        &
        set(
            map(
                int,
                input()
                .split()
            )
        )
    )
)
```

### Task 4 - in operator with sets

- **Description**: checking that element in set
- **Code Snippet**:

```python
# task.py
print("YES" if el in prev_elements_set else "NO")
```

### Task 5 - operator - , sets difference

- **Description** using operator - to get sets difference
- **code snippet**

```python
a_minus_b = a - b
```

### Task 6 - sets intersect

- **Description**: Use sets intersect
- **Code Snippet**:

```python
print(
    len(
        set(
            input_file
            .read()
            .split()
        )
    ),
    file=output_file
)
```

### Task 7 - sets union

- **Description**: Use sets union
- **Code Snippet**:

```python
negative_set |= set(question.split())
```

### Task 8 - sets union

- **Description**: Use sets union
- **Code Snippet**:

```python
negative_set |= set(question.split())
```

### Task 9 - Using sets practice

- **Description**: Use sets practice
- **Code Snippet**:

```python
for i in range(n):
    current_student_know_set = set()
    m = int(input())
    for j in range(m):
        current_student_know_set.add(input().strip())
    at_least_one_student_know_set |= current_student_know_set
    if all_students_know_set is None:
        all_students_know_set = current_student_know_set
    else:
        all_students_know_set = all_students_know_set
                                & current_student_know_set
```

### Task 10 - using dictionaries

- **Description:** using dictionaries
- **Code shippet**

```python
res.append(before_dict.get(word, 0))
before_dict[word] = before_dict.get(word, 0) + 1
```

### Task 11 - using dictionaries practice

- **Description:** using dictionaries practice
- **Code shippet**

```python
word1, word2 = input().split()
synonyms_dict[word1] = word2
synonyms_dict[word2] = word1
```

### Task 12 - dict.items() method

- **Description:** using dict.items() to get cortages of key-value pairs, which can be used in sorting or linear search
- **Code snippet:**

```python
print(
    min(words_count_dict.items(),
        key=lambda el: (-el[1], el[0]))[0], file=output_file)
```

### Task 13 - dict.items() method

- **Description:** using dict.items() to get cortages of key-value pairs, which can be used in sorting or linear search
- **Code snippet:**

```python
print(*map(lambda el: el[0], sorted(words_dict.items(),
                                    key=lambda el: (
                                        -el[1], el[0]))),
      file=output_file, sep="\n")
```


### Task 14 - deleting elements from dictionaries
- **Description:** using del dict[key] to delete dictionary elements
- **Code shippet**
```python
del candidates_dict[first_candidate]
```
