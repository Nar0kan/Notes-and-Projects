from createInput import Sort
from math import floor

class MergeSort(Sort):
    def __init__(self, *args) -> None:
        super().__init__(*args)
 

    def sortNumbers(self, array: list=[], order: str='ascending') -> None:
        self.order = order
        if not array:
            array = self.DATA

        if len(array) > 1:
            m = len(array)//2
            L = array[:m]
            R = array[m:]

            self.sortNumbers(array=L, order=self.order)
            self.sortNumbers(array=R, order=self.order)

            (rp, lp, k) = (0, 0, 0)

            while len(L)>lp and len(R)>rp:
                if L[lp] > R[rp]:
                    array[k] = R[rp]
                    rp+=1
                else:
                    array[k] = L[lp]
                    lp+=1
                k+=1
            
            while lp < len(L):
                array[k] = L[lp]
                lp+=1
                k+=1
            
            while rp < len(R):
                array[k] = R[rp]
                rp+=1
                k+=1

        if self.order == 'ascending':
            self.DATA = array
        elif self.order == 'descending':
            self.DATA = array[::-1]


    def sortSymbols(self, array: list=[], order: str='ascending') -> None:
        self.order = order
        if not array:
            array = self.DATA

        if len(array) > 1:
            r = len(array)//2
            L = array[:r]
            R = array[r:]

            self.sortNumbers(array=L, order=self.order)
            self.sortNumbers(array=R, order=self.order)

            # i - left pointer; j - right pointer; k - new array pointer
            (i, j, k) = (0, 0, 0)

            while i < len(L) and j < len(R):
                if ord(L[i]) < ord(R[j]):
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                array[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                array[k] = R[j]
                j += 1
                k += 1
        
        if self.order == 'ascending':
            self.DATA = array
        elif self.order == 'descending':
            self.DATA = array[::-1]


def main():
    OBJ = MergeSort()
    OBJ.createFile(symbols='numbers')
    OBJ.readFile()
    OBJ.sortNumbers(order='descending')
    OBJ.writeFile()


if __name__ == '__main__':
    main()