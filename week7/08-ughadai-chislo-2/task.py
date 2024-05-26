def main():
    max_n = int(input())
    positive_set = None
    negative_set = set()
    question = input()
    while question != 'HELP':
        pass


def f1(p_set: set, n_set: set, answer: str, max_n: int,
       question: str):
    temp_p_set, temp_n_set = p_set.copy(), n_set.copy()
    if answer == "YES":
        q = set(question.split())
        temp_p_set = q if temp_p_set is None else temp_p_set & q
    else:
        temp_n_set |= set(question.split())
    if p_set is None:
        result = set(map(str, range(1, max_n + 1))) - set(
            n_set)
    else:
        result = temp_p_set - temp_n_set
    return result


def f2(question: str, max_n: int):
    if max_n % 2 == 0 and question.split() == list(
            range(1, int(max_n / 2) + 1)):
        return True
    return False



if __name__ == "__main__":
    main()
