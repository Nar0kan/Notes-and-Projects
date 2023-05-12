def has_three_consecutive_double_letters(word: str) -> bool:
    counter, i = 0, 0
    j = len(word)-1

    while i < j:
        if word[i] == word[i+1]:
            counter += 1
            i += 1
            if not i == j:
                i += 1
        else:
            counter = 0
            i += 1
        if counter >= 3:
            return True
    
    return False


def main():
    print(has_three_consecutive_double_letters("abboobba"))     # True
    print(has_three_consecutive_double_letters("abbobba"))      # False
    print(has_three_consecutive_double_letters("abbooba"))      # False
    print(has_three_consecutive_double_letters("aboobba"))      # False
    print(has_three_consecutive_double_letters("abboobbaaaa"))  # True

    with open("words.txt", "r") as f:
        for line in f:
            word = line.strip("\n")
            if has_three_consecutive_double_letters(word):
                print(word)


if __name__ == "__main__":
    main()