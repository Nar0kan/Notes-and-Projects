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


def main() -> None:
    """
        Main function that's working when running the script directly.
    """
    words_list = read_file("words.txt")
    print(words_list[:20])


if __name__ == "__main__":
    main()
