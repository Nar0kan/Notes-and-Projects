from random import randint

class RSAEncrypt():
    def __init__(self, p: int=61, q: int=53):
        self.__p, self.__q = p, q
    

    @staticmethod
    def gcd(a, b) -> int:
        if a < b:
            for i in range(1, b+1):
                if b%i == 0 and a%i == 0:
                    res = i
        else:
            for i in range(1, a+1):
                if a%i == 0 and b%i == 0:
                    res = i
        return res


    @staticmethod
    def mod_inverse(a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return -1


    def generateKeys(self) -> None:
        self.n = self.__p*self.__q
        self.lambda_n = int(((self.__p-1)*(self.__q-1))/RSAEncrypt.gcd(self.__p-1, self.__q-1))
        #print(self.lambda_n)
        while True:
            self.e = randint(3, self.lambda_n-1)

            if RSAEncrypt.gcd(self.e, self.lambda_n) == 1:
                break
        
        self.d = RSAEncrypt.mod_inverse(self.e, self.lambda_n)
        #print(self.d)

    
    def encrypt(self, m: int) -> int:
        if m < self.n and m >= 0:
            self.m = m
        else:
            self.m = randint(0, self.n-1)
        
        self.c = (self.m**self.e)%self.n
        #print(self.c)
        return self.c


    def decrypt(self) -> int:
        self.m = (self.c**self.d)%self.n
        #print(self.m)
        return self.m


def main() -> None:
    OBJ = RSAEncrypt()
    OBJ.generateKeys()
    OBJ.encrypt(21)
    m = OBJ.decrypt()
    if m == 21:
        print("All good!")
    else:
        print("Something is wrong")


if __name__ == "__main__":
    main()