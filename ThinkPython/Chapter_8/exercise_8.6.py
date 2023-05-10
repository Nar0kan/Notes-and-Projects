def find(word: str, letter: str, start: int=0) -> int:
    index = start

    while index < len(word):
        if word[index] == letter:
            return index

        index = index + 1

    return -1


def countLetter(word: str, letter: str) -> int:
    count = 0
    a = 0

    while a <= len(word)-1:
        index = find(word, letter, a)

        if index >= 0:
            count += 1
            a += index + 1
        else:
            break
    
    print(count)
    return count


def test():
    countLetter("Wordpress", 's')
    countLetter("Wordpress", 'r')
    countLetter("Wordpress", 'e')
    countLetter("Wordpress", 'u')


if __name__ == "__main__":
    test()