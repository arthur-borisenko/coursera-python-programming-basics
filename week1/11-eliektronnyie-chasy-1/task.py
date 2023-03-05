def main():
    N = int(input())
    hours = (N // 60) % 24
    minutes = N % 60
    print(hours, minutes)


if __name__ == '__main__':
    main()
