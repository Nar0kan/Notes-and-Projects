from fruitfullFunctions import circleArea
from pointsDistance import findDistance


def findCircleArea(xc, yc, xp, yp) -> float:
    """
    Compute a circle area with given two points as
    a parameters. Center of a circle (xc, yc) and
    the point in parameter (xp, yp).
    """
    return circleArea(findDistance(xc, yc, xp, yp))


if __name__ == "__main__":
    print(findCircleArea(0, 0, 4, 0))