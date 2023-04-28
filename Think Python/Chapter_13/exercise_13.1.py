from pprint import pprint
from string import punctuation


def read_file(filename: str) -> list:
    """
        Reads a 'filename' file and stores the words in 'wordsList'
    """
    words_list = []

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            word = line[:-1]
            words_list.append(word)

    return words_list


def convert_to_lowercase(words: list) -> list:
    """
        Convert all the elements in the list in lowercase letters
    """
    lowercase_words = [i.lower() for i in words]

    return lowercase_words


def replace_punctuation(words: list) -> list:
    """
        Replace all the punctuation marks in the words to an empty string
    """
    for index, word in enumerate(words):
        for element in punctuation:
            if element in word:
                words[index] = words[index].replace(element, '')

    return words


def strip_whitespace(words: list) -> list:
    """
        Strip whitespace elements for every element in the 'words' list
    """
    for i, word in enumerate(words):
        words[i] = word.strip()

    return words


def main() -> None:
    """
        Main function that handles the proccess flow
    """
    words = read_file('words.txt')
    #pprint(words)

    words = convert_to_lowercase(words)
    #pprint(words)

    words = replace_punctuation(words)
    #pprint(words)

    words = strip_whitespace(words)
    pprint(words)




if __name__ == "__main__":
    main()
