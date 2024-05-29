from sys import stdin


class Matrix:
    def __init__(self, matrix):
        self.matrix = []
        for row in matrix:
            self.matrix.append(row.copy())

    def __str__(self):
        res = ""
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                res += str(self.matrix[i][j])
                if j != len(self.matrix[i]) - 1:
                    res += "\t"
            if i != len(self.matrix) - 1:
                res += "\n"
        return res

    def __add__(self, other):
        res = Matrix(self.matrix)
        for i in range(len(res.matrix)):
            for j in range(len(res.matrix[i])):
                res.matrix[i][j] += other.matrix[i][j]
        return res

    def __mul__(self, other):
        res = Matrix(self.matrix)
        for i in range(len(res.matrix)):
            for j in range(len(res.matrix[i])):
                res.matrix[i][j] *= other
        return res
    __rmul__ = __mul__

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))


if __name__ == "__main__":
    exec(stdin.read())
