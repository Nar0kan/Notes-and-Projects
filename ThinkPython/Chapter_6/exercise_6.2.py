from math import sqrt


def findHypotenuse(a, b) -> float:
    """
    Find hypotenuse of right-angle triangle.
    a and b are the legs of this triangle.
    """
    try:
        squareSum = a**2 + b**2
    except TypeError:
        return "a and b parameters must be float or int type."
    
    result = sqrt(squareSum)

    return result


print(findHypotenuse(3, 4))