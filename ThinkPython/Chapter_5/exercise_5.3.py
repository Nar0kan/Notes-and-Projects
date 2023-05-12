def checkFermat(a: int, b: int, c: int, n: int) -> None:
    if n <=2: return AttributeError("n must be greater than 2!")

    if (a**n+b**n == c^n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")


a = int(input("Input value for a: "))
b = int(input("Input value for b: "))
c = int(input("Input value for c: "))
n = int(input("Input value for n: "))
checkFermat(a, b, c, n)