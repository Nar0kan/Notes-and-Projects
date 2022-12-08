from createInput import Sort


class BubbleSort(Sort):
    def __init__(self, *args) -> None:
        super().__init__(*args)
    

    def sortNumbers(self) -> None:
        for j in range(self.amount):
            swapped = False

            for i in range(self.amount-j-1):
                if self.DATA[i] > self.DATA[i+1]:
                    self.DATA[i], self.DATA[i+1] = self.DATA[i+1], self.DATA[i]
                    swapped = True
            
            if not swapped:
                break


    def sortLetters(self) -> None:
        for j in range(self.amount):
            swapped = False

            for i in range(self.amount-j-1):
                if ord(self.DATA[i]) > ord(self.DATA[i+1]):
                    self.DATA[i], self.DATA[i+1] = self.DATA[i+1], self.DATA[i]
                    swapped = True
            
            if not swapped:
                break
            

    def sortAll(self) -> None:
        pass


def main() -> None:
    OBJ = BubbleSort()
    OBJ.createFile(symbols='letters')
    OBJ.readFile()
    OBJ.sortLetters()
    OBJ.writeFile()


if __name__ == '__main__':
    main()