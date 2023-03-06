def isBlack(pos: list) -> bool:
    # pos1[0]-x1 pos2[0]-x2 pos1[1]-y1 pos2[1]-y2
    return (pos[0] + pos[1]) % 2 == 0


def isDifferentColor(x1, y1, x2, y2):
    pos1 = [x1, y1]
    pos2 = [x2, y2]
    black1 = isBlack(pos1)
    black2 = isBlack(pos2)
    return not (black1 and black2 or not black1 and not black2)


def main():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    if isDifferentColor(x1, y1, x2, y2):
        print("NO")
    else:
        print("YES")


if __name__ == '__main__':
    main()
