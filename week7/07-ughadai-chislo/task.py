def main():
    max_n = int(input())
    positive_set = None
    negative_set = set()
    while True:
        question = input()
        if question == "HELP":
            break
        answer = input()
        if answer == "YES":
            q = set(question.split())
            positive_set = q if positive_set is None else positive_set & q
        else:
            negative_set |= set(question.split())
    if positive_set is None:
        result = set(map(str, range(1, max_n + 1))) - set(
            negative_set)
    else:
        result = positive_set - negative_set
    print(*sorted(result, key=lambda el: int(el)))


if __name__ == "__main__":
    main()
