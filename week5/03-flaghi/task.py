FLAG_LINES_TEMPLATE = ["+___ ",
                       "|{} / ",
                       "|__\\ ",
                       "|    "]


def main():
    n = int(input())
    result_lines = ["", "", "", ""]
    for i in range(n):
        for j in range(len(FLAG_LINES_TEMPLATE)):
            if j == 1:
                result_lines[j] += FLAG_LINES_TEMPLATE[j].format(
                    i + 1)
            else:
                result_lines[j] += FLAG_LINES_TEMPLATE[j]
    print("\n".join(result_lines))


if __name__ == "__main__":
    main()
