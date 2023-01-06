def countLetter(word: str, letter: str) -> int:
    count = 0

    for i in word:
        if i == letter:
            count += 1
    
    print(count)
    return count


def test():
    countLetter("Wordpress", 's')
    countLetter("Wordpress", 'r')
    countLetter("Wordpress", 'e')
    countLetter("Wordpress", 'u')


if __name__ == "__main__":
    test()