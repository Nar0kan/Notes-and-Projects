def uses_all(word: str, letters: str) -> bool:
    for i in letters:
        if i not in word:
            return False
    
    return True


def main() -> None:
    check_1 = ["master", "freedom", "cancel", "pleasure", "import"]

    print(uses_all(check_1[0], "restam"))   # True
    print(uses_all(check_1[1], "fredom"))   # True
    print(uses_all(check_1[2], "mcelcan"))  # False
    print(uses_all(check_1[3], "plesru"))  # False

    uses_aeiou = []
    uses_aeiouy = []

    with open("words.txt", "r") as f:
        for line in f:
            word = line.strip("\n")
            if uses_all(word, "aeiouy"):
                uses_aeiouy.append(word)
                uses_aeiou.append(word)
            elif uses_all(word, "aeiou"):
                uses_aeiou.append(word)

    print("\n\nUses aeiou: ", len(uses_aeiou))
    print("\nUses aeiouy: ", len(uses_aeiouy))


if __name__ == "__main__":
    main()