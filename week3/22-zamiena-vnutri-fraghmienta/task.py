FROM_PATTERN = "h"
TO_PATTERN = "H"


def replace_in_fragment(s: str, start: int, end: int, old: str,
                        new: str):
    fragment = s[start:end]
    replaced_fragment = fragment.replace(old, new)
    return s[:start] + replaced_fragment + s[end:]


def main():
    s = input()
    first = s.find(FROM_PATTERN)
    last = len(s) - s[::-1].find(FROM_PATTERN) - 1
    print(replace_in_fragment(s, first + 1, last, FROM_PATTERN,
                              TO_PATTERN))


if __name__ == '__main__':
    main()
