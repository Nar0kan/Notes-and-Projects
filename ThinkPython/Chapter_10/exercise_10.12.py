def findReversePairs(words: list) -> list:
    reversePairs = []
    words = words[:len(words)//16]  # Made a list a bit smaller

    for i in range(len(words)):
        reverseWord = words[i][::-1]
        if reverseWord in words[i+1:]:
            reversePairs.append(words[i])
    
    return reversePairs


def main() -> None:
    words = []

    with open("words.txt", "r") as f:
        for line in f:
            words.append(line.strip("\n"))
    
    print(findReversePairs(words))


if __name__ == "__main__":
    main()