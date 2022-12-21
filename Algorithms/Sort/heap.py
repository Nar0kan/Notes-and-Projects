from createInput import Sort


class HeapSort(Sort):
    def __init__(self, *args) -> None:
        super().__init__(*args)
    

    def heapifyNumbers(data, n, i) -> None:
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
    
        if l < n and data[i] < data[l]:
            largest = l
    
        if r < n and data[largest] < data[r]:
            largest = r

        if largest != i:
            data[i], data[largest] = data[largest], data[i]
            HeapSort.heapifyNumbers(data, n, largest)
    

    def heapifySymbols(data, n, i) -> None:
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
    
        if l < n and ord(data[i]) < ord(data[l]):
            largest = l
    
        if r < n and ord(data[largest]) < ord(data[r]):
            largest = r

        if largest != i:
            data[i], data[largest] = data[largest], data[i]
            HeapSort.heapifySymbols(data, n, largest)
 

    def sortNumbers(self, order: str='ascending') -> None:
        lenght = len(self.DATA)

        for i in range(lenght//2, -1, -1):
            HeapSort.heapifyNumbers(self.DATA, lenght, i)
    
        for i in range(lenght-1, 0, -1):
            self.DATA[i], self.DATA[0] = self.DATA[0], self.DATA[i]
            HeapSort.heapifyNumbers(self.DATA, i, 0)
        
        if order == 'descending':
            self.DATA = self.DATA[::-1]


    def sortSymbols(self, order: str='ascending') -> None:
        lenght = len(self.DATA)

        for i in range(lenght//2, -1, -1):
            HeapSort.heapifySymbols(self.DATA, lenght, i)
    
        for i in range(lenght-1, 0, -1):
            self.DATA[i], self.DATA[0] = self.DATA[0], self.DATA[i]
            HeapSort.heapifySymbols(self.DATA, i, 0)
        
        if order == 'descending':
            self.DATA = self.DATA[::-1]


def main() -> None:
    OBJ = HeapSort()
    OBJ.createFile(symbols='all', amount=1024)
    OBJ.readFile()
    OBJ.sortSymbols(order='descending')
    OBJ.writeFile()


if __name__ == '__main__':
    main()