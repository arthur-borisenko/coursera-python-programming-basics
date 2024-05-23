def main():
    n = int(input())
    village_list = list(input().split())
    m = int(input())
    bomb_list = list(input().split())
    for i in range(n):
        pos = village_list[i]
        village_list[i] = (int(pos), i + 1)
    for i in range(m):
        pos = bomb_list[i]
        bomb_list[i] = (int(pos), i + 1)
    village_list.sort(key=lambda i: i[0])
    bomb_list.sort(key=lambda i: i[0])
    res = []
    find_from = 0
    for i in range(n):
        village = village_list[i]
        left = None
        right = None
        for j in range(find_from, m):
            if bomb_list[j][0] >= village[0]:
                right = j
                break
            left = j
        if left is not None:
            find_from = left
        if right is None:
            res.append((bomb_list[left][1], village[1]))
        elif left is None:
            res.append((bomb_list[right][1], village[1]))
        else:
            if get_distance(village[0],
                            bomb_list[left][0]) < get_distance(
                village[0],
                    bomb_list[right][0]):
                res.append((bomb_list[left][1], village[1]))
            else:
                res.append((bomb_list[right][1], village[1]))
    res.sort(key=lambda i: i[1])
    res = map(lambda el: el[0], res)
    print(*res)


def get_distance(x1, x2):
    return abs(x1 - x2)


if __name__ == "__main__":
    main()
