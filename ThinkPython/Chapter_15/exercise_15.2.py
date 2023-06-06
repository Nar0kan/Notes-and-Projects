class Point(object):
    """
        Class that represents a points in two dimentsions
    """


class Rectangle(object):
    """
        Represents rectangle with height, width and corner coordinates
    """


def move_rectangle(rectangle, dx, dy) -> None:
    rectangle.corner.x += dx
    rectangle.corner.y += dy


def main() -> None:
    """
        Main script function.
    """
    rectangle = Rectangle()
    rectangle.height, rectangle.width, rectangle.corner = 20, 20, Point()

    rectangle.corner.x, rectangle.corner.y = 2, 2
    print(f"Coordinates of the corner before the move ({rectangle.corner.x}, {rectangle.corner.y})")

    move_rectangle(rectangle, 10, -8)
    print(f"Coordinates of the corner after the move ({rectangle.corner.x}, {rectangle.corner.y})")


if __name__ == "__main__":
    main()
