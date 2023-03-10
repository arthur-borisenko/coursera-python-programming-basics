def sign(x):
    # returns sign :D
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1


def main():
    x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
    if sign(x1) == sign(x2) and sign(y1) == sign(y2):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
