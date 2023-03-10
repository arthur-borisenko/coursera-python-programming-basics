def main():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    partY = y1 == y2 + 1 or y1 == y2 - 1 or y1 == y2
    partX = x1 == x2 + 1 or x1 == x2 - 1 or x1 == x2
    if partX and partY:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
