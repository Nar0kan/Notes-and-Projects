from string import ascii_letters


def rotate_word(sequence: str, n: int=20) -> str:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
    result = ""
    sequence = sequence.lower()

    for i in sequence:
        if alphabet.find(i) < len(alphabet)-n:
            result += alphabet[alphabet.find(i)+n]
        else:
            result += alphabet[len(alphabet) - alphabet.find(i) - n]
    
    print(result)
    return result


def test():
    rotate_word("AmongUs")
    rotate_word("mellon", -10)
    rotate_word("cheer", 7)


if __name__ == "__main__":
    test()