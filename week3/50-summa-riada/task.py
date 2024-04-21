def euclidean_greatest_common_divider_algorithm(a: int, b: int) -> int:
    prev_r = max(a, b)
    r = min(a, b)
    while r != 0:
        next_r = prev_r % r
        prev_r = r
        r = next_r
    return prev_r


def lowest_common_multiple(a: int, b: int) -> int:
    return int(a * b / euclidean_greatest_common_divider_algorithm(a, b))


def safe_lowest_common_multiple_for_multiple_numbers(numbers: list[int]) -> int:
    if len(numbers) == 1:
        return numbers[0]
    a = numbers[0]
    b = numbers[1]
    prev_lcm = lowest_common_multiple(a, b)
    for i in range(2, len(numbers)):
        prev_lcm = lowest_common_multiple(prev_lcm, numbers[i])
    return prev_lcm
def if_integer_then_to_int(n:float):
    if n.is_integer():
        return int(n)
    return n
def main():
    n=int(input())
    dividers=[]
    for i in range(1,n+1):
        dividers.append(i**2)
    lcm= safe_lowest_common_multiple_for_multiple_numbers(dividers)
    summa=0
    for divider in dividers:
        summa+=lcm/divider
    print(if_integer_then_to_int(summa/lcm))
if __name__ == '__main__':
    main()