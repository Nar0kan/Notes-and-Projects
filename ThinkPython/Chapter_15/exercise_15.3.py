from copy import deepcopy


class Point(object):
    """
        Class that represents a points in two dimentsions
    """


class Rectangle(object):
    """
        Represents rectangle with height, width and corner coordinates
    """


def move_rectangle(rectangle, dx, dy) -> Rectangle:
    new_rectangle = deepcopy(rectangle)
    
    new_rectangle.corner.x += dx
    new_rectangle.corner.y += dy

    return new_rectangle


def main() -> None:
    """
        Main script function.
    """
    rectangle = Rectangle()
    rectangle.height, rectangle.width, rectangle.corner = 20, 20, Point()

    rectangle.corner.x, rectangle.corner.y = 2, 2
    new_rectangle = move_rectangle(rectangle, 10, -8)

    print(f"Coordinates of the old rectangle ({rectangle.corner.x}, {rectangle.corner.y})")
    print(f"Coordinates of the new rectangle ({new_rectangle.corner.x}, {new_rectangle.corner.y})")
    
    # To show that they are different objects
    #print(new_rectangle is rectangle)
    #print(new_rectangle == rectangle)
    #print(new_rectangle.corner == rectangle.corner)

if __name__ == "__main__":
    main()
