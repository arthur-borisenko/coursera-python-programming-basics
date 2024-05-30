FLAG_LINES_TEMPLATE = ["+___ ",
                       "|{} / ",
                       "|__\\ ",
                       "|    "]


def safe_format(s, *args):
    args = list(map(str, args))
    args_count = min(s.count("{"), s.count("}"))
    return s.format(*args[:args_count])


def main():
    n = int(input())
    result_lines = ["", "", "", ""]
    for i in range(n):
        for j in range(len(FLAG_LINES_TEMPLATE)):
            result_lines[j] += safe_format(FLAG_LINES_TEMPLATE[j],
                                           i + 1)
    print("\n".join(result_lines))


if __name__ == "__main__":
    main()
