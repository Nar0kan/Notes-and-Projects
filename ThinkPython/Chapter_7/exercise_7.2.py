def square_root(a: int, x: int, epsilon: float=0.0000001) -> int:
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        else:
            x = y
    
    return y


def test():
    print(square_root(1, 4))
    print(square_root(4, 3))
    print(square_root(16, 5))
    print(square_root(25, 8))


if __name__ == "__main__":
    test()