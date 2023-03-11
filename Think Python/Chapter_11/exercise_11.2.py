def histogram(word: str) -> dict:
    result = dict()

    for letter in word:
        result[letter] = result.get(letter, 0) + 1
    
    return result


def main() -> None:
    h = histogram("entry")
    print(h)

if __name__=="__main__":
    main()