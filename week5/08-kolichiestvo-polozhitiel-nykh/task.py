def main():
    input_list = input().split(" ")
    positive_count = 0
    for element in input_list:
        if int(element) > 0:
            positive_count += 1
    print(positive_count)


if __name__ == "__main__":
    main()
