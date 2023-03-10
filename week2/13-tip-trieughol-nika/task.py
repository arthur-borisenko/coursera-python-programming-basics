def main():
    import math
    a, b, c = int(input()), int(input()), int(input())
    if a == 0 or b == 0 or c == 0:
        print("impossible")
        return
    aa = a * a
    bb = b * b
    cc = c * c
    try:
        alpha0 = (aa + bb - cc) / (a * b * 2)
        beta0 = (aa + cc - bb) / (a * c * 2)
        yeta0 = (bb + cc - aa) / (b * c * 2)
        alpha = math.acos(alpha0) / math.pi * 180
        beta = math.acos(beta0) / math.pi * 180
        yeta = math.acos(yeta0) / math.pi * 180
    except:
        print("impossible")
        return
    maxAngle = max(alpha, beta, yeta)
    if 90 < maxAngle < 180:
        print("obtuse")
    elif maxAngle == 90:
        print("rectangular")
    elif maxAngle < 90:
        print("acute")
    else:
        print("impossible")


if __name__ == '__main__':
    main()
