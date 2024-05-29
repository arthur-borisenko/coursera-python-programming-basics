import sys
import copy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    id = 0

    def __init__(self, matrix):
        self.id += 1
        self.matrix = copy.deepcopy(matrix)

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
        if self.size() != other.size():
            raise MatrixError(self, other)
        else:
            res = Matrix(self.matrix)
            for i in range(len(res.matrix)):
                for j in range(len(res.matrix[i])):
                    res.matrix[i][j] += other.matrix[i][j]
            return res

    @staticmethod
    def transposed(obj):
        new_matrix = []
        for i in range(obj.size()[1]):
            new_matrix.append([])
            for j in range(obj.size()[0]):
                new_matrix[i].append(None)
        for i in range(len(obj.matrix)):
            for j in range(len(obj.matrix[i])):
                new_matrix[j][i] = obj.matrix[i][j]
        return Matrix(new_matrix)

    def determinant(self):
        if self.size()[0] != self.size()[1]:
            raise ValueError
        elif self.size()[0] == 2:
            return self.matrix[0][0] * self.matrix[1][1] - \
                self.matrix[0][1] * self.matrix[1][0]
        elif self.size()[0] > 2:
            result = 0
            for i in range(self.size()[0]):
                minor_matrix = copy.deepcopy(self.matrix)
                del minor_matrix[0]
                for minor_i in range(len(minor_matrix)):
                    del minor_matrix[minor_i][i]
                minor = Matrix(minor_matrix)
                minor_determinant = minor.determinant()
                if i % 2 == 0:
                    result += minor_determinant * self.matrix[0][i]
                else:
                    result -= minor_determinant * self.matrix[0][i]

            return result

    def solve(self, b_vector):
        pass
        determinant = self.determinant()
        if determinant == 0:
            raise ValueError
        else:
            solution = []
            for i in range(self.size()[0]):
                a_i = copy.deepcopy(self.matrix)
                for a_i_i in range(len(a_i)):
                    for a_i_j in range(len(a_i[a_i_i])):
                        if a_i_j == i:
                            a_i[a_i_i][a_i_j] = b_vector[a_i_i]
                a_i_matrix = Matrix(a_i)
                a_i_determinant = a_i_matrix.determinant()
                solution.append(a_i_determinant / determinant)
        return solution

    def transpose(self):
        new_matrix = self.transposed(self)
        self.matrix = new_matrix.matrix
        return new_matrix

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
    exec(sys.stdin.read())
