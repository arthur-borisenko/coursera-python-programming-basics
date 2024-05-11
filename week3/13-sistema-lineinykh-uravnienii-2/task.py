import enum


def safe_to_int(n):
    if n.is_integer():
        return int(n)
    else:
        return n


class SolutionTypes(enum.Enum):
    No = 0
    Inf_px_plus_q = 1
    One = 2
    Inf_x_is_constant_y_any = 3
    Inf_y_is_constant_x_any = 4
    Inf_any = 5


def solve_linear_equation_system(a_matrix, b_vector):
    """
    in task, we have linear equation system:

    ax+by=e
    cx+dy=f

    <=>
    a_00*x+a_01*y=b_0
    a_10*x+a_11*y=b_1

    where we choose non-null x coefficient and name it a_00 if it
    exists,else not change.

    :param a_matrix: [[a, b], [c, d]] - equation system coefficients
    :param b_vector: [e, f] -- constant terms
    :return: type,roots
    """
    (a, b), (c, d) = a_matrix[0], a_matrix[1]
    (e, f) = b_vector
    if a == 0:
        a_10, a_11, b_1 = a, b, e
        a_00, a_01, b_0 = c, d, f
    else:
        a_00, a_01, b_0 = a, b, e
        a_10, a_11, b_1 = c, d, f
    if a_00 == 0:
        # non-null x coefficient is not exists
        # than we have equation system:
        # a_01*y=b_0
        # a_11*y=b_1
        if a_01 == 0:
            if b_0 == 0:
                if a_11 == 0:
                    if b_1 == 0:
                        return [SolutionTypes.Inf_any]
                    else:
                        return [SolutionTypes.No]
                else:
                    return [SolutionTypes.Inf_y_is_constant_x_any,
                            safe_to_int(b_1 / a_11)]
            else:
                return [SolutionTypes.No]
        else:
            if a_11 == 0:
                if b_1 == 0:
                    return [SolutionTypes.Inf_y_is_constant_x_any,
                            safe_to_int(b_0 / a_01)]
                else:
                    return [SolutionTypes.No]
            else:
                if b_0 / a_01 == b_1 / a_11:
                    return [SolutionTypes.Inf_y_is_constant_x_any,
                            safe_to_int(b_0 / a_01)]
                else:
                    return [SolutionTypes.No]
    else:
        if a_01 * a_10 / a_00 - a_11 == 0:
            if b_0 * a_10 / a_00 - b_1 != 0:
                return [SolutionTypes.No]
            else:
                if a_01 == 0:
                    return [SolutionTypes.Inf_x_is_constant_y_any,
                            safe_to_int(b_0 / a_00)]
                else:
                    return [SolutionTypes.Inf_px_plus_q,
                            safe_to_int(-a_00 / a_01),
                            safe_to_int(b_0 / a_01)]
        else:
            y = (b_1 - b_0 * a_10 / a_00) / (
                    a_11 - a_10 * a_01 / a_00)
            x = (b_0 - a_01 * y) / a_00
            return [SolutionTypes.One, safe_to_int(x), safe_to_int(y)]


def main():
    a, b, c = float(input()), float(input()), float(input())
    d, e, f = float(input()), float(input()), float(input())
    res = solve_linear_equation_system([[a, b], [c, d]], [e, f])
    res[0] = res[0].value
    print(" ".join(map(str, res)))


if __name__ == '__main__':
    main()
