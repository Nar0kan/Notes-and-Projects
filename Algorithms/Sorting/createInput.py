from random import randint
from string import ascii_letters

class Sort:
    def __init__(self, option: str="numbers") -> None:
        if option == "numbers":
            self.from_=-5096
            self.to=5096
            self.amount=512
        elif option == "letters":
            self.alphabet = ascii_letters
        elif option == "all":
            self.alphabet = "".join(chr(x) for x in range(32,127))



    def sortNumbers(self):
        SEPARATOR = ', '
        NUMBERS = SEPARATOR.join([str(randint(self.from_, self.to)) for i in range(self.amount)])
        FILENAME = "input.txt"

        with open(FILENAME, "w") as f:
            f.write(NUMBERS)
        
        with open('input.txt', 'r') as f:
            NUMBERS = f.read()

        DATA = NUMBERS.split(', ')
        for n in range(0, len(DATA)):
            DATA[n] = int(DATA[n])
    
        with open('output.txt', 'w') as f:
            f.write(', '.join([str(i) for i in DATA]))