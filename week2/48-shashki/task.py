def isChethnoe(N: int) -> bool:
    return N % 2 == 0


class directions:
    FORWARD = 0
    BACKWARD = 1
    LEFT = 2
    RIGHT = 3


def check_move_directions_and_distances(x1, x2, y1, y2):
    x_dist = abs(x1 - x2)
    y_dist = abs(y1 - y2)
    if x1 < x2:
        x_dir = directions.RIGHT
    else:
        x_dir = directions.LEFT
    if y1 < y2:
        y_dir = directions.FORWARD
    else:
        y_dir = directions.BACKWARD
    return x_dir, y_dir, x_dist, y_dist


def main():
    x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
    x_dir, y_dir, x_dist, y_dist = check_move_directions_and_distances(x1, x2,
                                                                       y1, y2)
    if (isChethnoe(x_dist) == isChethnoe(y_dist) and y_dir ==
            directions.FORWARD):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
