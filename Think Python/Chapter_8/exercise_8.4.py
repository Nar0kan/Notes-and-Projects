def find(word: str, letter: str, start: int=0) -> int:
    index = start

    while index < len(word):
        if word[index] == letter:
            return index

        index = index + 1

    return -1


def test():
    a = 'Some word'
    print(find(a, 'o', 2))
    print(find(a, 'o', 1))
    print(find(a, 'x', 2))


if __name__ == "__main__":
    test()