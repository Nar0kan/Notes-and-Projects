from math import sqrt


def findDistance(x1, y1, x2, y2) -> float:
    """
    Takes two points (x1, y1), (x2, y2) as parameters
    and finds distance between them. Return float value.
    """
    return sqrt(((x2-x1)**2)+((y2-y1)**2))



if __name__ == "__main__":
    print(findDistance(1, 2, 4, 6))
    print(findDistance(1, 3, 1, 6))