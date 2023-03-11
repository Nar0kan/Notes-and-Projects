def histogram(word: str) -> dict:
    result = dict()

    for letter in word:
        result[letter] = result.get(letter, 0) + 1
    
    return result


def print_hist(someDict: dict) -> None:
    keys = someDict.keys()

    for key in sorted(keys):
        print(key, someDict[key])


def main() -> None:
    h = histogram("entry")
    print_hist(h)
    print("_"*5)

    h = histogram("library")
    print_hist(h)
    print("_"*5)

    h = histogram("absurd")
    print_hist(h)

if __name__=="__main__":
    main()