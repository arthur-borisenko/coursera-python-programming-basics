def main():
    N = int(input())
    seconds = N % 60
    if seconds < 10:
        result_seconds = "0" + str(seconds)
    else:
        result_seconds = seconds
    minutes = N // 60 % 60
    if minutes < 10:
        result_minutes = "0" + str(minutes)
    else:
        result_minutes = str(minutes)
    hours = N // 3600 % 24
    print(str(hours) + ":" + str(result_minutes) + ":" + str(result_seconds))


if __name__ == '__main__':
    main()
