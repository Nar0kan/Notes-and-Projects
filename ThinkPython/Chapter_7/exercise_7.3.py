from math import sqrt


def square_root(a: int, x: int=5, epsilon: float=0.0000001) -> int:
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        else:
            x = y
    
    return y


def drawTable(value) -> None:
    print(value, square_root(value), sqrt(value), abs(square_root(value)-sqrt(value)), sep="\t", end="\n")


def test() -> None:
    for i in range(1, 10):
        drawTable(i)


if __name__ == "__main__":
    test()