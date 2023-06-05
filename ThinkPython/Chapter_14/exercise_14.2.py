from os import path


def read_file(filename: str) -> str:
    """
        Reads a file 'filename' in the current folder,
        returns the text from this file. Handles Type and
        IO (file) errors
    """
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            text = f.read()
        return text
    except TypeError:
        print("TypeError occured. Check that arguments and variables are correct types.")
    except IOError:
        print("Something is wrong with file handling. Please, try again.")
        if path.exists(filename):
            print(f"Check if the '{filename}' file exists in this '{path.curdir}' folder")
        if not path.isfile(filename):
            print(f"Check if the '{filename}' file is correct and if it is a file!")

    return ''


def write_file(filename: str, text: str) -> None:
    """
        Writes a text from 'text' variable to a file 'filename'
        in the current folder. Handles the errors that may occure.
    """
    try:
        with open(filename, 'w', encoding="utf-8") as f:
            text = f.write(text)
    except TypeError:
        print("TypeError occured. Check that arguments and variables are correct types.")
    except IOError:
        print("Something is wrong with file handling. Please, try again.")
        if not path.exists(filename):
            print(f"Check if the '{filename}' file exists in this '{path.curdir}' folder")
            return None
        if not path.isfile(filename):
            print(f"Check if the '{filename}' file is correct and if it is a file!")
            return None
    
    return None


def capitalize_lines(text: str, splitter: str=" ") -> str:
    """
        Capitalize each line in a text, after spliting it with
        an 'splitter' (\n) for file text.
    """
    new_text = []

    for line in text.split(splitter):
        new_text.append(line.capitalize())
    
    return splitter.join(new_text)



def sed(pattern: str, replacement: str, filename1: str, filename2:str) -> None:
    pattern, replacement = pattern.lower(), replacement.lower()
    
    text = read_file(filename1).lower()

    if text:
        text = text.replace(pattern, replacement)
        text = capitalize_lines(text, splitter="\n")

        write_file(filename2, text)
    else:
        print("Program has been stopped due to an error!")
    
    return None


def main() -> None:
    """
        Main function that's working when running the script directly.
    """
    pattern = "SHOULD REPLACE"
    replacement = "In my mind"
    filename1 = "GlimpseOfUsLyrics.txt"
    filename2 = "GlimpseOfUsLyricsChanged.txt"
    sed(pattern, replacement, filename1, filename2)


if __name__ == "__main__":
    main()
