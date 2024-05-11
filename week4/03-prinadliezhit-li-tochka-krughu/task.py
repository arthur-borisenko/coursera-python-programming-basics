import math


def main():
    x, y, xc, yc, r = float(input()), float(input()), float(
        input()), float(input()), float(input())
    if IsPointInCircle(x, y, xc, yc, r):
        print("YES")
    else:
        print("NO")


def get_distance(point1, point2):
    x_distance = abs(point1[0] - point2[0])
    y_distance = abs(point1[1] - point2[1])
    distance = math.sqrt(x_distance ** 2 + y_distance ** 2)
    return distance


def IsPointInCircle(x, y, xc, yc, r):
    center = (xc, yc)
    point = (x, y)
    distance = get_distance(center, point)
    return distance <= r


if __name__ == "__main__":
    main()
