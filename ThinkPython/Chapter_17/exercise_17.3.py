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


def main() -> None:
    """
        The main function in the script
    """
    point_1 = Point(2.5, 2)
    print(f"The coordinates of the point_1 are: {point_1}")

    point_2 = Point()
    print(f"The coordinates of the point_2 are initials: {point_2}")


if __name__ == "__main__":
    main()
