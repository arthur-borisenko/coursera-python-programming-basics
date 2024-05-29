# Week 9 - Python Programming Basics

## Overview
This week focuses on classes and exceptions in Python. Below is a detailed description of each task for Week 9.
### Learning Objectives
* Basics of defining and using classes in Python.
* Inheritance and polymorphism.
* Handling and raising exceptions.
## Task Descriptions

### Task 1 - Classes in Python
- **Description**: 
- Basic class structures, attributes, and methods. 
- defining methods such as __str__ to make standard functions such as str() work with class
- **Code Snippet**:
```python
    # task.py
class Matrix:
    def __init__(self, matrix):
        ...
    def str(self):
        ...
        return ...
   ```

### Task 2 - defining methods such as __add__ to make class support operands
- **Description**: Using operands calls class methods, some of them were defined in this task
- **Code Snippet**:
```python
# task.py
class Matrix:
    def __init__(self):
        ...
    def __add__(self, other):
        ...
        return ...
```

### Task 3 - creating and raising exceptions
- **Description**: creating custom exceptions and raising them
- **Code Snippet**:
```python
# task.py
class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
class Matrix:
    def __init__(self):
        ...
    def size(self):
        return ...
    def __add__(self, other):
        if self.size() != other.size():
            raise MatrixError(self, other)
        ...
        return ...
```

### Task 4 - Custom Exceptions
- **Description**: creating custom exceptions and raising them
- **Code Snippet**:
```python
# task.py
class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
```
