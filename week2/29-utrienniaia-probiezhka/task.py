def main():
    FirstDayDistance = int(input())
    TargetDistance = int(input())
    currentDay = 1
    currentDistance = FirstDayDistance
    while currentDistance < TargetDistance:
        currentDay += 1
        currentDistance *= 1.1
    print(currentDay)


if __name__ == '__main__':
    main()
