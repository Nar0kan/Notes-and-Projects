from createInput import Sort


class QuickSort(Sort):
    def __init__(self, *args) -> None:
        super().__init__(*args)
 

    def partitionNumbers(self, data, left, right) -> int:
        pivot = data[right]
        i = left - 1

        for j in range(left, right):
            if data[j] <= pivot:
                i = i + 1
                data[i], data[j] = data[j], data[i]
            
        data[i+1], data[right] = data[right], data[i+1]

        return i + 1
    

    def partitionSymbols(self, data, left, right) -> int:
        pivot = ord(data[right])
        i = left - 1

        for j in range(left, right):
            if ord(data[j]) <= pivot:
                i = i + 1
                data[i], data[j] = data[j], data[i]
            
        data[i+1], data[right] = data[right], data[i+1]
        
        return i + 1


    def sortNumbers(self, order: str='ascending', left: int=0, right: int=0) -> None:
        if left < right:
            pivot = self.partitionNumbers(self.DATA, left, right)
            self.sortNumbers(self.DATA, left, pivot-1)
            self.sortNumbers(self.DATA, pivot+1, right)

        return self.DATA if order == 'ascending' else self.DATA[::-1]


    def sortSymbols(self, order: str='ascending', left: int=0, right: int=0) -> None:
        if left < right:
            pivot = self.partitionSymbols(self.DATA, left, right)
            self.sortSymbols(self.DATA, left, pivot-1)
            self.sortSymbols(self.DATA, pivot+1, right)

        return self.DATA if order == 'ascending' else self.DATA[::-1]


def main():
    OBJ = QuickSort()
    OBJ.createFile(symbols='all')
    OBJ.readFile()
    OBJ.sortSymbols(order='descending', right=len(OBJ.DATA)-1)
    OBJ.writeFile()


if __name__ == '__main__':
    main()