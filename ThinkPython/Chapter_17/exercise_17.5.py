class Point(object):
    """
        Represents a point in 2 dimensions
        atributes: x, y
    """
    def __init__(self, x: float=0, y: float=0) -> None:
        self.x, self.y = x, y


    def get_coordinates(self) -> tuple:
        """
            Gets the current coordinates of the point and returns them
        """
        return self.x, self.y


    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple) or isinstance(other, list) and len(other) == 2:
            self.x += other[0]
            self.y += other[1]
            return Point(self.x, self.y)
        elif isinstance(other, dict):
            self.x += other['x']
            self.y += other['y']
            return Point(self.x, self.y)
        else:
            raise ValueError("The argument must be a Point, dictionary, list or tuple")


    def __radd__(self, other):
        return self.__add__(other)


def main() -> None:
    """
        The main function in the script
    """
    point_1 = Point(2.5, 2)
    print(f"The coordinates of the point_1 are: {point_1}")

    point_2 = Point(1, 2.5)
    print(f"The coordinates of the point_2 are: {point_2}")

    print(point_1 + point_2)
    print(point_1 + (1, 1))
    print(point_1 + [1, 1])
    print(point_2 + {"x": 2, "y": 2})
    print((0, 10) + point_2)


if __name__ == "__main__":
    main()
