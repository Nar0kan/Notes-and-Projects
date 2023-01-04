def isPower(a: int, b: int) -> bool:
    return True if any([i**a==b for i in range(b)]) else False


def test():
    print(isPower(2, 4))
    print(isPower(3, 8))
    print(isPower(2, 5))
    print(isPower(2, 25))
    print(isPower(3, 25))


if __name__ == "__main__":
    test()