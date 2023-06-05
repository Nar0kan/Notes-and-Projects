from exercise_12_4_as_module import readFile, printAnagrams
import shelve


def store_anagrams(filename: str="database", anagrams: dict={}) -> None:
    """
        Stores an anagrams dictionary in database file in a shelf.
    """
    assert anagrams, "anagrams parameter must be a dictionary with keys and values!"

    db_file = shelve.open(filename)

    for key, value in anagrams.items():
        db_file[key] = value

    db_file.close()


def read_anagrams(filename: str="database") -> dict:
    """
        Reads a filename that stores an anagrams dictionary and returns
        it.
    """
    anagrams = {}

    with shelve.open(filename) as db_file:
        for key in db_file:
            anagrams[key] = db_file[key]

    return anagrams


def main() -> None:
    """
        Main function that's working when running the script directly.
    """
    filename = "C:/Coding/Notes-and-Projects/ThinkPython/Chapter_12/words.txt"
    words = readFile(filename)
    anagram_list = printAnagrams(words)
    anagram_dict = {}

    for anagram in anagram_list:
        anagram_dict[anagram[0]] = anagram[1:]

    store_anagrams("database", anagram_dict)
    stored_anagrams = read_anagrams()

    # Check if what I stored is what I saved previously
    print(stored_anagrams == anagram_dict)

    #print(stored_anagrams)
    #print(anagram_dict)


if __name__ == "__main__":
    main()
