def main():
    data = deserialize()
    print("YES") if case(data) else print("NO")


def deserialize():
    box1 = (int(input()), int(input()), int(input()))
    box2 = (int(input()), int(input()), int(input()))
    container = (int(input()), int(input()), int(input()))
    return (box1, box2), container


def case(inputData) -> bool:
    (boxes, cont) = inputData
    box1states = (boxes[0], (boxes[0][1], boxes[0][0], boxes[0][2]))
    box2states = (boxes[1], (boxes[1][1], boxes[1][0], boxes[1][2]))
    stackStates = (0, 1, 2)  # ("alongX", "alongY", "alongZ")
    for box1 in box1states:
        for box2 in box2states:
            for stack_along_axis in stackStates:
                result = isStatePossible(box1, box2, cont, stack_along_axis)
                if result:
                    return True
    return False


def isStatePossible(box1, box2, cont, stack_along_axis):
    for axis in range(3):
        result = plusOrMax(box1, box2, axis, stack_along_axis) <= cont[axis]
        if not result:
            return False
    return True


def plusOrMax(box1, box2, axis, stackAlongAxis):
    if stackAlongAxis == axis:
        return box1[axis] + box2[axis]
    else:
        return max(box1[axis], box2[axis])


if __name__ == '__main__':
    main()
