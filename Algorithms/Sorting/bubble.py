from createInput import Sort


class BubbleSort(Sort):
    def __init__(self, *args) -> None:
        super().__init__(*args)
    

    def sortNumbers(self, order: str='ascending') -> None:
        for j in range(self.amount):
            swap = False

            for i in range(self.amount-j-1):
                if self.DATA[i] > self.DATA[i+1]:
                    self.DATA[i], self.DATA[i+1] = self.DATA[i+1], self.DATA[i]
                    swap = True
            
            if not swap:
                break
        
        if order == 'descending':
            self.DATA=self.DATA[::-1]


    def sortSymbols(self, order: str='ascending') -> None:
        for j in range(self.amount):
            swap = False

            for i in range(self.amount-j-1):
                if ord(self.DATA[i]) > ord(self.DATA[i+1]):
                    self.DATA[i], self.DATA[i+1] = self.DATA[i+1], self.DATA[i]
                    swap = True
            
            if not swap:
                break
        
        if order == 'descending':
            self.DATA=self.DATA[::-1]


def main() -> None:
    OBJ = BubbleSort()
    OBJ.createFile(symbols='all')
    OBJ.readFile()
    OBJ.sortSymbols(order='descending')
    OBJ.writeFile()


if __name__ == '__main__':
    main()