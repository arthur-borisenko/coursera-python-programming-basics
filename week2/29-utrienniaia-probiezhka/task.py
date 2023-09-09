def main():
    first_day_distance = int(input())
    target_distance = int(input())
    current_day = 1
    current_distance = first_day_distance
    while current_distance < target_distance:
        current_day += 1
        current_distance *= 1.1
    print(current_day)


if __name__ == '__main__':
    main()
