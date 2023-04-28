from pprint import pprint
from string import punctuation


def read_file(filename: str) -> list:
    """
        Reads a 'filename' file, begins to read from the start of the book
        and stores the lines in 'lines_list'
    """
    lines_list = []

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line_str = line[:-1]
            if line_str:
                lines_list.append(line_str)

    for index, line in enumerate(lines_list):
        if "*** START OF THE PROJECT GUTENBERG EBOOK" in line:
            lines_list = lines_list[index+1:]
            break

    return lines_list


def separate_to_words(lines: list):
    """
        Separates the words in the 'lines' list and returns
        this 'words' list
    """
    words = []

    for line in lines:
        for word in line.split(' '):
            if word:
                words.append(word)

    return words


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
        for element in str(punctuation + '’”“—'):  # '’' symbol is not in standart ASCII table so I added it manually
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


def count_words(words: list):
    """
        Function to count the words amount in the book for each word and total
    """
    counter = dict()
    keys = counter.keys()
    total = 0

    for word in words:
        total += 1
        if word in keys:
            counter[word] += 1
        else:
            counter[word] = 1
    
    return counter, total


def read_books(list_of_books: list) -> None:
    """
        Read the books from the list_of_books to get the words and count them to compare
    """
    assert list_of_books, "No books selected!"

    for book in list_of_books:
        print(f"Current book: {book}")
        lines = read_file(book)
        #pprint(lines)

        words = separate_to_words(lines)
        #pprint(words[:50])

        words = convert_to_lowercase(words)
        #pprint(words[:50])

        words = replace_punctuation(words)
        #pprint(words[:50])

        words = strip_whitespace(words)
        print("Words used in the book:\n")

        counter_dict, total = count_words(words)
        for key in counter_dict:
            print(key, counter_dict[key])

        print(f"Total amount of words in the book: {total}\n\n")


def main() -> None:
    """
        Main function that handles the proccess flow
    """
    read_books(list_of_books=["Alices_Adventures_in_Wonderland.txt", "The_Adventures_of_Ferdinand_Count_Fathom.txt", "The_Enchanted_April.txt", "The_Picture_of_Dorian_Gray.txt"])


if __name__ == "__main__":
    main()
