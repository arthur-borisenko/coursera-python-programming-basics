def safe_to_int(n):
    if n.is_integer():
        return int(n)
    else:
        return n


def solve_linear_equation_system(a_matrix, b_vector):
    """
    in task, we have linear equation system,
    that has exactly one solution:

    ax+by=e
    cx+dy=f

    <=>
    a_00*x+a_01*y=b_0
    a_10*x+a_11*y=b_1

    where we choose non-null x coefficient and name it a_00.
    Such non-null coefficient exists,
    because system has exactly one solution

    :param a_matrix: [[a, b], [c, d]] - equation system coefficients
    :param b_vector: [e, f] -- constant terms
    :return: x, y - solution
    """

    (a, b), (c, d) = a_matrix[0], a_matrix[1]
    (e, f) = b_vector
    if a != 0:
        a_00, a_01, b_0 = a, b, e
        a_10, a_11, b_1 = c, d, f

    else:
        a_10, a_11, b_1 = c, d, f
        a_00, a_01, b_0 = a, b, e
    y = (b_1 - b_0 * a_10 / a_00) / (a_11 - a_10 * a_01 / a_00)
    x = (e - b * y) / a
    return x, y


def main():
    a, b, c = float(input()), float(input()), float(input())
    d, e, f = float(input()), float(input()), float(input())
    x, y = solve_linear_equation_system([[a, b], [c, d]], [e, f])
    print(safe_to_int(x), safe_to_int(y))


if __name__ == '__main__':
    main()
