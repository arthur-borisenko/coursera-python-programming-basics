def main():
    def process(boxes):
        smaller_index = None  # index of smaller box. 0 if equal. -1 on error
        box1 = sorted(boxes[0])
        box2 = sorted(boxes[1])
        for i in range(0, 3):
            side1 = box1[i]
            side2 = box2[i]
            if smaller_index is None or smaller_index == 0:
                if side1 < side2:
                    smaller_index = 1
                if side1 == side2:
                    smaller_index = 0
                if side2 < side1:
                    smaller_index = 2
            elif smaller_index == 1:
                if not (side1 <= side2):
                    smaller_index = -1
                    break
            elif smaller_index == 2:
                if not (side2 <= side1):
                    smaller_index = -1
                    break
        return smaller_index

    boxes = [[int(input()), int(input()), int(input())],
             [int(input()), int(input()), int(input())]]

    result = process(boxes)
    if result == 0:
        print("Boxes are equal")
    elif result == 1:
        print("The first box is smaller than the second one")
    elif result == 2:
        print("The first box is larger than the second one")
    elif result == -1:
        print("Boxes are incomparable")


if __name__ == '__main__':
    main()
