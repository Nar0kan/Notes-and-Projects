def isDoubleInterlocked(word_1: str, word_2: str, num: int=2) -> bool:
    for i in range(len(word_1)//2):
        if word_2 == word_1[i:][::num]:
            return True
    
    return False


def findInterlockPairs(someList: list, num: int, max: int=2) -> list:
    pairs = {}

    for word in someList:
        pairs[word] = []

    for word in someList:
        count, i = len(pairs[word]), 0

        while count < max and i < len(someList):
            if len(word) > len(someList[i]) and isDoubleInterlocked(word, someList[i], num) and len(pairs[word]) < max and someList[i] not in pairs[word]:
                pairs[word].append(someList[i])
                count+=1

            elif len(word) < len(someList[i]) and isDoubleInterlocked(someList[i], word, num) and len(pairs[someList[i]]) < max and word not in pairs[someList[i]]:
                pairs[someList[i]].append(word)
            
            i+=1

    return [(i, pairs[i]) for i in pairs if len(pairs[i])==max]


def main() -> None:
    list_1 = ["claymore", "bay", "may", "lay", "way", "staly", "praly", "ray", "yay", "may", "say", "rl", "cam", "mr", "sl", "my", "pay", "pl", "by", "tl", "a"]
    print(isDoubleInterlocked("hello", "hlo"))
    print(isDoubleInterlocked("hello", "el"))
    print(isDoubleInterlocked("hello", "h"))
    print(findInterlockPairs(list_1, 2))
    print(findInterlockPairs(list_1, 3, 2))


if __name__ == "__main__":
    main()