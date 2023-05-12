def has_no_e(word: str) -> bool:
    return True if not "e" in word else False


def main():
    check_1 = ["password", "form", "engage", "asteroid", "uniform"]
    for i in check_1:
        print(i, " has no 'e': ", has_no_e(i))
    
    words, check_2 = [], []

    with open("words.txt", "r") as f:
        for i in f:
            words.append(i[:i.find("\n")])
            if has_no_e(i):
                check_2.append(i[:i.find("\n")])
            
    print("\n\nTotal words: ", len(words), "\tAmount of words without the 'e' letter: ", len(check_2))
    print("\n\n", float(len(check_2)/len(words)), " - is the percentage of words with no e in words.txt")


if __name__ == "__main__":
    main()