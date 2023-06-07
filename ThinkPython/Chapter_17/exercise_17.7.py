class Kangaroo:
    def __init__(self, name, pouch_contents: list=[]) -> None:
        self.name = name
        self.pouch_contents = pouch_contents


    def put_in_pouch(self, something) -> None:
        """
            Adds a new item to the pouch contents.
        """
        self.pouch_contents.append(something)


    def __str__(self) -> str:
        t = [ self.name + ' has pouch contents:' ]

        for obj in self.pouch_contents:
            s = '\t' + object.__str__(obj)
            t.append(s)

        return '\n'.join(t)


def main():
    """
        The main function in the script.
    """
    kanga = Kangaroo("Kanga")
    roo = Kangaroo("Roo")

    kanga.put_in_pouch(roo)
    roo.put_in_pouch("Tablet")
    kanga.put_in_pouch(727)

    print(kanga)
    print(roo)


if __name__ == '__main__':
    main()
