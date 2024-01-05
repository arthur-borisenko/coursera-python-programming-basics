def main():
    seq = get_seq()
    seq.remove(max(seq))
    print(max(seq))


def get_seq():
    result = []
    n = int(input())
    while n != 0:
        result.append(n)
        n = int(input())
    return result


if __name__ == '__main__':
    main()
