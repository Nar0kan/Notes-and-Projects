def is_abecedarian(word: str) -> bool:
    if sorted(word) == [i for i in word]:
        return True
    return False


def is_abecedarian_recursion(word: str) -> bool:
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian_recursion(word[1:])


def main():
    print(is_abecedarian_recursion("ace"))    # True
    print(is_abecedarian("ape"))    # False
    print(is_abecedarian_recursion("bee"))    # True
    print(is_abecedarian("iq"))     # True
    print(is_abecedarian_recursion("coding")) # False

    countAbecedarian = 0

    with open("words.txt", "r") as f:
        for line in f:
            word = line.strip("\n")
            if is_abecedarian(word):
                countAbecedarian += 1
                #print(word)
    
    print("\n\nAbecedatian words total: ", countAbecedarian)


if __name__ == "__main__":
    main()