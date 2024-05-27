def main():
    with open("input.txt", encoding="utf-8") as input_file, open(
            "output.txt", "w", encoding="utf-8") as output_file:
        candidates_dict = {}
        votes = 0
        for candidate in input_file:
            candidate = candidate.strip()
            votes += 1
            candidates_dict[candidate] = candidates_dict.get(
                candidate, 0) + 1
        selected_candidate = None
        for candidate in candidates_dict.items():
            if candidate[1] * 2 > votes:
                selected_candidate = candidate[0]
        if selected_candidate is None:
            first_candidate = \
                max(candidates_dict.items(), key=lambda el: el[1])[0]
            del candidates_dict[first_candidate]
            second_candidate = \
                max(candidates_dict.items(), key=lambda el: el[1])[0]
            print(first_candidate, second_candidate, sep="\n",
                  file=output_file)
        else:
            print(selected_candidate, file=output_file)


if __name__ == "__main__":
    main()
