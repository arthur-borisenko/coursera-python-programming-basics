def main():
    n = int(input())
    synonyms_dict = {}
    for i in range(n):
        word1, word2 = input().split()
        synonyms_dict[word1] = word2
        synonyms_dict[word2] = word1
    word = input()
    print(synonyms_dict[word])


if __name__ == "__main__":
    main()
