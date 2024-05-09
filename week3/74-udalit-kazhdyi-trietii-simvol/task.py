def main():
    input_file = open("input.txt")
    output_file = open("output.txt", "w")
    try:
        s = input_file.read()
        res = ""
        for i in range(len(s)):
            if i % 3 != 0:
                res += s[i]
        output_file.write(res)
    finally:
        input_file.close()
        output_file.close()


if __name__ == "__main__":
    main()
