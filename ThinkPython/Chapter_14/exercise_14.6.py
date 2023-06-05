import urllib


def main() -> None:
    """
        Main function that's working when running the script directly.
    """
    conn = urllib.urlopen('http://thinkpython.com/secret.html')
    for line in conn:
        print(line.strip())


if __name__ == "__main__":
    main()
