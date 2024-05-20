def main():
    n = int(input())
    input_list = input().split()
    x = int(input())
    min_distance = n
    min_distance_value = None
    for num in input_list:
        distance = get_distance(int(num), x)
        if distance < min_distance:
            min_distance = distance
            min_distance_value = num
    print(min_distance_value)
    pass


def get_distance(a, b):
    return abs(a - b)


if __name__ == "__main__":
    main()
