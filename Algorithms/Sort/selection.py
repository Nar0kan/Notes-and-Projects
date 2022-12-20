from createInput import Sort


class SelectionSort(Sort):
    def __init__(self, *args) -> None:
        super().__init__(*args)
 

    def sortNumbers(self, order: str='ascending') -> None:
        for i in range(len(self.DATA)):
            min = i

            for j in range(i+1, len(self.DATA)):
                if self.DATA[min] > self.DATA[j]:
                    min = j
            
            self.DATA[i], self.DATA[min] = self.DATA[min], self.DATA[i]
        
        return self.DATA if order == 'ascending' else self.DATA[::-1]


    def sortSymbols(self, order: str='ascending') -> None:
        for i in range(len(self.DATA)):
            min = i

            for j in range(i+1, len(self.DATA)):
                if ord(self.DATA[min]) > ord(self.DATA[j]):
                    min = j
            
        self.DATA[i], self.DATA[min] = self.DATA[min], self.DATA[i]
        
        return self.DATA if order == 'ascending' else self.DATA[::-1]


def main():
    OBJ = SelectionSort()
    OBJ.createFile(symbols='all')
    OBJ.readFile()
    OBJ.sortSymbols(order='ascending')
    OBJ.writeFile()


if __name__ == '__main__':
    main()