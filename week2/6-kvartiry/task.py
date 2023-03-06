def main():
    x, y = int(input()), int(input())
    apartmentsOnEntrace = y - x + 1
    if (x - 1) % apartmentsOnEntrace == 0:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
