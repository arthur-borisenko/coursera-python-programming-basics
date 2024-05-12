def main():
    print(get_seq_sum())
    pass


def get_seq_sum(prev=0):
    n = int(input())
    if n != 0:
        return get_seq_sum(prev + n)
    else:
        return prev


if __name__ == "__main__":
    main()
