def main():
    n = int(input())
    input_list = list(map(int, input().split()))
    print(*sorted(input_list))
    pass


if __name__ == "__main__":
    main()
