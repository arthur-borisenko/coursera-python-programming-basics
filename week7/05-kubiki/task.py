def main():
    with open("input.txt", encoding="utf-8") as input_file, open(
            "output.txt", "w", encoding="utf-8") as output_file:
        n, m = input_file.readline().split()
        a = set()
        b = set()
        for i in range(int(n)):
            a.add(int(input_file.readline()))
        for i in range(int(m)):
            b.add(int(input_file.readline()))

        a_intersect_b = a & b
        print(len(a_intersect_b), file=output_file)
        print(*sorted(a_intersect_b), file=output_file)

        a_minus_b = a - b
        print(len(a_minus_b), file=output_file)
        print(*sorted(a_minus_b), file=output_file)

        b_minus_a = b - a
        print(len(b_minus_a), file=output_file)
        print(*sorted(b_minus_a), file=output_file)


if __name__ == "__main__":
    main()
