from createInput import Sort


class InsertionSort(Sort):
    def __init__(self, *args) -> None:
        super().__init__(*args)
 

    def sortNumbers(self, order: str='ascending') -> None:
        for step in range(1, len(self.DATA)):
            i = step - 1
            next = self.DATA[step]
             
            while i >= 0 and next < self.DATA[i]:
                self.DATA[i+1] = self.DATA[i]
                i = i - 1
            
            self.DATA[i+1] = next

        return self.DATA if order=='ascending' else self.DATA[::-1]


    def sortSymbols(self, order: str='ascending') -> None:
        for step in range(1, len(self.DATA)):
            i = step - 1
            next = self.DATA[step]
             
            while i >= 0 and ord(next) < ord(self.DATA[i]):
                self.DATA[i+1] = self.DATA[i]
                i = i - 1
            
            self.DATA[i+1] = next

        return self.DATA if order=='ascending' else self.DATA[::-1]


def main():
    OBJ = InsertionSort()
    OBJ.createFile(symbols='numbers')
    OBJ.readFile()
    OBJ.sortNumbers(order='ascending')
    OBJ.writeFile()


if __name__ == '__main__':
    main()