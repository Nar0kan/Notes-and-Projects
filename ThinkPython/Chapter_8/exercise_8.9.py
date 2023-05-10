def is_reverse(word1: str, word2: str) -> bool:
    """Checks if the word1 is the reverse version
    of word2, where both words are given as parameters."""

    if len(word1) != len(word2):
        return False
    
    word1, word2 = word1.lower(), word2.lower()
    i = 0
    j = len(word2)-1

    while j >= 0:
        print(i, j)

        if word1[i] != word2[j]:
            return False
        
        i = i+1
        j = j-1
    
    return True


def test():
    print(is_reverse("AraAra", "araara"))
    print(is_reverse("AraAra", "araare"))
    print(is_reverse("AraAra", "3raara"))
    print(is_reverse("AraAra", "ara"))
    print(is_reverse("AraAra", "Cause"))


if __name__ == "__main__":
    test()