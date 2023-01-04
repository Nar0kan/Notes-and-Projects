from math import pi


def absoluteValue(x):
    try:
        if x < 0:
            return -x
        else:
            return x
    except TypeError:
        try:
            return absoluteValue(float(x))
        except ValueError:
            return "x parameter must be either float or integer"


def circleArea(radius) -> float:
    return radius**2*pi


if __name__ == "__main__":
    print(circleArea(2))
    print(absoluteValue('2'))