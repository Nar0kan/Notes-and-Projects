from createInput import Sort


class HeapSort(Sort):
    def __init__(self, *args) -> None:
        super().__init__(*args)
 

    def sortNumbers(self, order: str='ascending') -> None:
        pass


    def sortSymbols(self, order: str='ascending') -> None:
        pass


def main():
    OBJ = HeapSort()
    OBJ.createFile(symbols='numbers')
    OBJ.readFile()
    OBJ.sortNumbers()
    OBJ.writeFile()


if __name__ == '__main__':
    main()