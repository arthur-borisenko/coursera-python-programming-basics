def main():
    seq = input().split(" ")
    r = []
    for i in range(0, len(seq), 2):
        r.append(seq[i])
    print(*r)


if __name__ == "__main__":
    main()
