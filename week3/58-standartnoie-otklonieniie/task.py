import math


class InputIntStream:
    def __init__(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        self.current = int(input())
        if self.current != 0:
            return self.current
        raise StopIteration


def main():
    result = get_standard_deviation(InputIntStream())
    print(result)


def get_standard_deviation(input_stream):
    # formula σ=sqrt(((x₁² + ... + xn²) + (n * s²) - 2 * (x₁ + ...
    # + xn) * s) / (n-1)), which is used in solution is obtained
    # from formula σ=sqrt( (x₁² + s² - 2 * x₁ * s+...+xn²+s² - 2 *
    # xn * s) / (n - 1)), which is obtained from the formula
    # σ=sqrt(((x₁-s)²+(x₂ -s)²+…+( xn-s)²) / (n-1)) by opening
    # parentheses before the squares, in all formulas sqrt is
    # square root, s - arithmetic average
    elements_sum = 0
    elements_count = 0
    elements_squares_sum = 0
    for el in input_stream:
        elements_count += 1
        elements_sum += el
        elements_squares_sum += el ** 2
    average = elements_sum / elements_count
    result = math.sqrt((elements_squares_sum -
                        2 * average * elements_sum +
                        elements_count * average ** 2) /
                       (elements_count - 1))
    return result


if __name__ == '__main__':
    main()
