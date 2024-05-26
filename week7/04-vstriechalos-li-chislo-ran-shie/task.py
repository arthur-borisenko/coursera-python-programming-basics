def main():
    input_list = input().split()
    prev_elements_set = set()
    for el in input_list:
        print("YES" if el in prev_elements_set else "NO")
        prev_elements_set.add(el)


if __name__ == "__main__":
    main()
