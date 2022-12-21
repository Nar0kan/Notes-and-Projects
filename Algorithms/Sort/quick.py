from createInput import Sort


class QuickSort(Sort):
    def __init__(self, *args) -> None:
        super().__init__(*args)
 

    @staticmethod
    def partitionNumbers(data, left, right) -> int:
        pivot = data[right]
        i = left - 1

        for j in range(left, right):
            if data[j] <= pivot:
                i = i + 1
                data[i], data[j] = data[j], data[i]
            
        data[i+1], data[right] = data[right], data[i+1]

        return i + 1
    

    @staticmethod
    def partitionSymbols(data, left, right) -> int:
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
            pivot = QuickSort.partitionNumbers(self.DATA, left, right)
            self.sortNumbers(self.DATA, left, pivot-1)
            self.sortNumbers(self.DATA, pivot+1, right)

        if order == 'descending':
            self.DATA = self.DATA[::-1]


    def sortSymbols(self, order: str='ascending', left: int=0, right: int=0) -> None:
        if left < right:
            pivot = QuickSort.partitionSymbols(self.DATA, left, right)
            self.sortSymbols(self.DATA, left, pivot-1)
            self.sortSymbols(self.DATA, pivot+1, right)

        if order == 'descending':
            self.DATA = self.DATA[::-1]


def main() -> None:
    OBJ = QuickSort()
    OBJ.createFile(symbols='all')
    OBJ.readFile()
    OBJ.sortSymbols(order='descending', right=len(OBJ.DATA)-1)
    OBJ.writeFile()


if __name__ == '__main__':
    main()