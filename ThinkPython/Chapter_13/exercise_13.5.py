from random import choice
from string import punctuation, whitespace


def skip_header(file_text: str) -> str:
    """
        Skips the header information of the Gutenberg Project books.
    """
    for line in file_text:
        if line.startswith("*** START OF THE PROJECT GUTENBERG EBOOK"):
            return file_text
    
    return file_text



def read_book(filename: str, skip_header_value: bool=True) -> list:
    """
        Read a GP book, skipping the header information if
        skip_header_value == True (by default it's True)
        and return stripped words from the book without
        punctuations and whitespaces at the start and end.
    """
    words_list = []

    with open(filename, "r", encoding="utf-8") as file_text:
        if skip_header_value:
            file_text = skip_header(file_text)
        for line in file_text:
            words = line.strip(punctuation + whitespace + "!`'/.\"~@#$%^&*()_+,<>")
            if words:
                for word in words.split(" "):
                    if "--" not in word:
                        word = word.strip(punctuation + whitespace)
                        words_list.append(word.lower())
                    else:
                        for i in word.split("--"):
                            words_list.append(i.lower())
                    
    return words_list


def choose_from_hist(hist: dict) -> str:
    """
        Chooses random value from a 'hist' with propotional
        chance which is the value of the element (int) divided
        by total amount of words (each element is multiplied
        to it`s value, because this is the histogram)
    """
    words = []
    total = 0

    for word in hist:
        for i in range(hist[word]):
            words.append(word)
            total += 1

    random_word = choice(words)
    chance = hist[random_word]/total

    return random_word, chance


def histogram(words):
    """
        Creates a histogram for 'words' list
    """
    d = dict()

    for word in words:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    
    return d


def main() -> None:
    """
        Main function that's working when running the script directly.
    """
    words = read_book("pg70899.txt")
    
    hist = histogram(words)

    for i in range(10):
        word, chance = choose_from_hist(hist)
        print(word, chance)


if __name__=="__main__":
    main()
