def main():
    l1, r1, l2, r2, l3, r3 = int(input()), int(input()), int(input()), int(
        input()), int(input()), int(input())
    match1 = (l1, r1)
    match2 = (l2, r2)
    match3 = (l3, r3)
    print(matchToBeMoved(match1, match2, match3))


def matchToBeMoved(match1, match2, match3):
    if ((dist(match1, match2) == 0 and dist(match1, match3) == 0) or (
            dist(match1, match2) == 0 and dist(match2, match3) == 0) or (
            dist(match1, match3) == 0 and dist(match1, match2) == 0) or (
            dist(match1, match3) == 0 and dist(match3, match2) == 0) or (
            dist(match2, match3) == 0 and dist(match2, match1) == 0) or (
            dist(match2, match3) == 0 and dist(match3, match1) == 0)):
        return 0
        # let match 1 should be moved
    if matchCond(match1, match2, match3):
        return 1
        # let match 2 should be moved
    if matchCond(match2, match1, match3):
        return 2
        # let match 3 should be moved
    if matchCond(match3, match1, match2):
        return 3
    return -1


def matchCond(matchA, matchB, matchC):
    return dist(matchB, matchC) <= length(matchA)


def edgeInside(coord, match):
    return match[0] <= coord <= match[1]


def dist(matchA: (), matchB: ()):
    if (edgeInside(matchA[0], matchB) or edgeInside(matchA[1], matchB)) or (
            edgeInside(matchB[0], matchA) or edgeInside(matchB[1], matchA)):
        return 0
    else:
        if matchA[0] > matchB[0]:
            lmatch = matchB
            rmatch = matchA
        else:
            lmatch = matchA
            rmatch = matchB
        return rmatch[0] - lmatch[1]


def length(match):
    return match[1] - match[0]


if __name__ == '__main__':
    main()
