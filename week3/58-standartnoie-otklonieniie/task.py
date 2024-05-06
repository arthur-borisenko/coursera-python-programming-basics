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
    """
        from task we need to find the standard deviation by formula:
        sqrt(((x₁-s)²+(x₂-s)²+…+(xn-s)²)/(n-1))
        <=>
        sqrt((x₁²-2*x₁*s+s²...+xn²-2*xn*s+s²)/(n-1))
        <=>
        sqrt(((x₁²+...+xn²)-2*(x₁+...+xn)*s+(n*s²))/(n-1))
        <=>
        {
            sqrt(((elements_squares_sum)-2*(elements_sum)*s+(elements_count*s²))/(elements_count-1))
            elements_squares_sum=x₁²+...+xn²
            elements_sum=x₁+...+xn
            elements_count=n
        }

        :param input_stream:
        :return:
        """
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
