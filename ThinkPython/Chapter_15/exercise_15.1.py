from math import sqrt


class Point(object):
    """
        Class that represents a points in two dimentsions
    """


def calculate_distance_between_points(point_1, point_2):
    return sqrt((point_2.x - point_1.x)**2+(point_2.y-point_1.y)**2)


def main() -> None:
    """
        Main script function.
    """
    point_1 = Point()
    point_1.x, point_1.y = 2, 3

    point_2 = Point()
    point_2.x, point_2.y = 5, 6

    print(f"The distance between point ({point_1.x}, {point_1.y}) and point ({point_2.x}, {point_2.y}) is: ")
    print(calculate_distance_between_points(point_1, point_2))


if __name__ == "__main__":
    main()
