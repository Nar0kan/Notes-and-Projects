from os import walk
from pprint import pprint


def main() -> None:
    """
        Main function that's working when running the script directly.
    """
    pprint([(root, files) for root, dirs, files in walk('..')])


if __name__ == "__main__":
    main()
