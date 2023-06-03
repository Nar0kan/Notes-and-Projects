from string import punctuation, whitespace
from random import choice


def skip_header(file_text: str) -> str:
    """
        Skips the header information of the Gutenberg Project books.
    """
    for line in file_text:
        if line.startswith("*** START OF THE PROJECT GUTENBERG EBOOK"):
            return file_text
    
    return file_text


def read_file(filename: str, skip_header_value: bool=True) -> list:
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
            words = line.strip(punctuation + whitespace + "!`'/.\"~@#$%^&*()_+")
            if words:
                for word in words.split(" "):
                    if "--" not in word:
                        word = word.strip(punctuation + whitespace)
                        words_list.append(word.lower())
                    else:
                        for i in word.split("--"):
                            words_list.append(i.lower())
                    
    return words_list


def count_words(words_list: list) -> tuple:
    """
        Count total number of words and the number of times each
        word is used in words_list variable.
    """
    words_dictionary = dict()
    total = 0

    for word in words_list:
        if word not in words_dictionary:
            words_dictionary[word] = 1
        else:
            words_dictionary[word] += 1
        total += 1
    
    return total, words_dictionary


def main() -> None:
    """
        Main function that's working when running the script directly.
    """
    words_list = read_file("pg70899.txt")
    print(words_list[:20])

    total, words_dictionary = count_words(words_list)
    print(f"Total amount of words: {total}")

    for i in range(20):
        random_word, count = choice(list(words_dictionary.items()))
        print(f"Word {random_word} appears {count} times")


if __name__ == "__main__":
    main()
