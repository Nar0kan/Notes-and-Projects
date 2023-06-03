from string import punctuation, whitespace


def read_file(filename: str) -> list:
    """
        Reads a file text and for each line, represented by a single word
        strips punctuation and whitespaces to add into words_list variable.
        Returns this words_list.
    """
    words_list = []

    with open(filename, "r", encoding="utf-8") as file_text:
        for line in file_text:
            word = line.strip(punctuation + whitespace)
            words_list.append(word)

    return words_list


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
            line = line.replace('-', ' ')
            words = line.strip(punctuation + whitespace + "!`'/.\"~@#$%^&*()_+")
            if words:
                for word in words.split(" "):
                    word = word.strip(punctuation + whitespace)
                    if word:
                        words_list.append(word.lower())
                    
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
    book_words_list = read_book("pg70899.txt")
    words_list = read_file("words.txt")

    book_total, book_words_dictionary = count_words(book_words_list)
    total, words_dictionary = count_words(words_list)
    print(f"Total amount of words in the book: {book_total}")
    print(f"Total amount of words in the book: {total}")

    book_words_set = set(book_words_list)
    words_set = set(words_list)

    different_words = book_words_set - words_set

    print("Words that are in the book but not in the words list: ", different_words)


if __name__ == "__main__":
    main()
