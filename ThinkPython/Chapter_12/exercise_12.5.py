def consist_of(line_1: str, line_2: str) -> bool:
    if sorted(line_1) == sorted(line_2):
        return True
    return False


def readFile() -> list:
    words = dict()

    with open("words.txt", "r") as f:
        for line in f:
            word = line.strip("\n")
            length = len(word)
            try:
                words[length].append(word)
            except KeyError:
                words.setdefault(length, [word])
    
    return words


def checkMetathesis(word_1: str, word_2: str) -> bool:
    if not consist_of(word_1, word_2):
        return False

    letters_1 = dict(zip(word_1, range(len(word_1))))
    letters_2 = dict(zip(word_2, range(len(word_2))))

    counter = 0
    for i in letters_1:
        if letters_1[i] != letters_2[i]:
            counter += 1
    
    return True if counter == 2 else False


def metathesisPairs(fwords: dict) -> list:
    """ It's working, but is very slow with a big dictionaries of data """
    res = []
    words = fwords[3]

    for word in words:
        for temp in range(len(words)):
            checkWord = words[temp]
            if checkMetathesis(checkWord, word):
                res.append((checkWord, word))

    # for length in words:
    #     for word in words[length]:
    #         for temp in range(len(words[length])):
    #             checkWord = words[length][temp]
    #             if checkMetathesis(checkWord, word):
    #                 res.append((checkWord, word))

    return res


def main() -> None:
    words = readFile()
    print(metathesisPairs(fwords = words))
    #print(checkMetathesis("reserve", "reverse"))
    #print(checkMetathesis("reserve", "revers"))
    #print(checkMetathesis("resrve", "revese"))
    #print(checkMetathesis("reserv", "revers"))


if __name__ == "__main__":
    main()