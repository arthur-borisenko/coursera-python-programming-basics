def choco(in1, in2, in3):
    enough = in1 * in2 >= in3
    inSide1 = in3 % in1 == 0
    inSide2 = in3 % in2 == 0
    if enough and (inSide2 or inSide1):
        print('YES')
    else:
        print('NO')


def main():
    in1 = int(input())
    in2 = int(input())
    in3 = int(input())
    choco(in1, in2, in3)


if __name__ == '__main__':
    main()
