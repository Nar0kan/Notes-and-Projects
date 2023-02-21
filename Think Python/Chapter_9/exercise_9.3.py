def avoids(word: str, forbidden: str) -> bool:
    for i in word:
        if i in forbidden:
            return False
        
    return True


def main():
    check_1 = ["seasalt", "peanut", "almond", "cream", "ice", "estate"]
    
    for word in check_1:
        print(word, " avoids 'ea': ", avoids(word=word, forbidden="ea"))
        print(word, " avoids 'ck': ", avoids(word=word, forbidden="ck"))
    
    check_2 = str(input("Write your forbidden letters: "))
    numberOfWords = 0

    with open("words.txt", "r") as f:
        for word in f:
            j = word.strip("\n")
            if avoids(j, check_2):
                numberOfWords += 1
    
    print("Number of words that don't contains any of ", check_2, " letters is: ", numberOfWords)

    check_3 = "abcdefghijklmnopqrstuvwxyz"
    lettersDict = {}

    for letter in check_3:
        numberOfWords = 0

        with open("words.txt", "r") as f:
            for word in f:
                j = word.strip("\n")
                if avoids(j, letter):
                    numberOfWords += 1

        lettersDict[letter] = numberOfWords
    
    lettersDict = sorted(lettersDict.items(), key=lambda x:x[1])

    print(lettersDict)


if __name__ == "__main__":
    main()