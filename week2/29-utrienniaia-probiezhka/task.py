def main():
    Start = int(input())
    Need = int(input())
    currentDay = 0
    currentDistance = Start
    while currentDistance < Need:
        currentDay += 1
        currentDistance *= 1.1
    print(currentDay + 1)


if __name__ == '__main__':
    main()
