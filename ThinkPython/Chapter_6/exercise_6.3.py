def isBetween(x, y, z) -> bool:
    return x <= y and y <= z


if __name__ == "__main__":
    print(isBetween(1, 2, 3))
    print(isBetween(2, 2, 3))
    print(isBetween(3, 2, 3))