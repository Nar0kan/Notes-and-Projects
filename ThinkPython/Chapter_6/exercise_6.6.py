def first(word: str) -> str:
    return word[0]


def last(word: str) -> str:
    return word[-1]


def middle(word: str) -> str:
    return word[1:-1]


def isPalindrome(word: str) -> bool:
    if len(word) > 2 and first(word)==last(word):
        return isPalindrome(middle(word))
    elif (len(word) == 2 and first(word)==last(word)) or len(word)==1:
        return True
    return False
    


def test():
    print(middle('iv')) # None, cause -1 and 1 are the same and -1 not included
    print(middle('r'))  # None, cause -1 not included
    print(middle(''))   # None, cause no characters at all
    print(isPalindrome('astra'))
    print(isPalindrome('banana'))
    print(isPalindrome('araara'))
    print(isPalindrome('a'))
    print(isPalindrome('ab'))

if __name__ == "__main__":
    test()