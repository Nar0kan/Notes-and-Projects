from random import randint, choice
from string import ascii_letters


class Sort:
    def __init__(self) -> None:
        return None
    

    def createFile(self, filename: str='input.txt', symbols: str='numbers', amount: int=512) -> None:
        self.filename = filename
        self.amount = amount
        self.symbols = symbols

        if symbols == "numbers":
            self.from_ = -10192
            self.to = 10192
            SEPARATOR = ', '
            DATA = SEPARATOR.join([str(randint(self.from_, self.to)) for i in range(self.amount)])
        elif symbols == "letters":
            self.alphabet = ascii_letters
            DATA = ''.join([choice(self.alphabet) for i in range(self.amount)])
        elif symbols == "all":
            self.alphabet = "".join(chr(x) for x in range(32,127))
            DATA = ''.join([choice(self.alphabet) for i in range(self.amount)])
        else:
            raise ValueError("option value must be str in ['numbers', 'letters', 'all']")
        
        with open(self.filename, "w") as f:
            f.write(DATA)
    

    def readFile(self) -> None:
        with open(self.filename, 'r') as f:
            SYMBOLS = f.read()
        
        if self.symbols == "numbers":
            self.DATA = SYMBOLS.split(', ')
            for n in range(0, len(self.DATA)):
                self.DATA[n] = int(self.DATA[n])
        else:
            self.DATA = [i for i in SYMBOLS]


    def writeFile(self, filename: str='output.txt') -> None:
        if self.symbols == "numbers":
            with open(filename, 'w') as f:
                f.write(', '.join([str(i) for i in self.DATA]))
        else:
            with open(filename, 'w') as f:
                f.write(''.join([str(i) for i in self.DATA]))


if __name__ == "__main__":
    OBJ = Sort()
    OBJ.createFile(symbols='letters')
    OBJ.readFile()
    OBJ.writeFile()