def main():
    hours_1, minutes_1, seconds_1 = int(input()), int(input()), int(input())
    hours_2, minutes_2, seconds_2 = int(input()), int(input()), int(input())
    secs = calc_seconds(hours_2, minutes_2, seconds_2) \
        - calc_seconds(hours_1, minutes_1, seconds_1)
    print(secs)


def calc_seconds(hours, minutes, seconds):
    return hours * 60 * 60 + minutes * 60 + seconds


if __name__ == '__main__':
    main()
