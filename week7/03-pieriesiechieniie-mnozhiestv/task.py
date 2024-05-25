def main():
    print(*sorted(set(map(int, input().split())) & set(
        map(int, input().split()))))
    pass


if __name__ == "__main__":
    main()
