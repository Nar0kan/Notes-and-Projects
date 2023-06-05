from pprint import pprint


def readFile(filename: str) -> list:
    words = []

    with open(filename, "r") as f:
        for line in f:
            words.append(line.strip("\n"))
    
    return words


def printAnagrams(wordList: list, output: int=3) -> list:
    d = dict()
    for i in wordList:
        k = ''.join(sorted(i))
        d.setdefault(k, [i])

        if i not in d[k]:
            d[k].append(i)
    
    res = []
    if output==2:
        lengthDict = dict()
        for key in d:
            val = d[key]
            lengthDict.setdefault(len(val), list(tuple(val)))
            lengthDict[len(val)].append(tuple(val))
        
        for length in sorted(lengthDict, reverse=True):
            for el in lengthDict[length]:
                res.append(el)

    elif output==3:
        for key in d:
            if len(d[key]) > 7:
                res.append((d[key]))
    else:
        for key in d:
            if len(d[key]) > 1:
                res.append((d[key]))
    
    return res


def main() -> None:
    words = readFile()
    pprint(printAnagrams(words))


if __name__ == "__main__":
    main()
