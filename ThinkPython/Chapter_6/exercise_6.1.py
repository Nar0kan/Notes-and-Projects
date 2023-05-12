def compareValues(x, y) -> int:
    try:
        x, y = float(x), float(y)
    except ValueError:
        return "x and y must be either integers or float"
    
    if x > y:
        return 1
    elif x < y:
        return -1
    
    return 0


if __name__ == "__main__":
    print(compareValues(1, 2))
    print(compareValues(2, 1))
    print(compareValues(1, 1))
    print(compareValues('a', '2'))
    print(compareValues('2', '3'))