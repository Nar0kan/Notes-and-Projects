from swampy.World import World


class Point(object):
    """
        Class that represents a points in two dimentsions
    """


class Rectangle(object):
    """
        Represents a rectangle with height, width and corner coordinates
    """


class Circle(object):
    """
        Represents a circle with the radius and the center point
    """


def draw_rectangle(canvas, rectangle) -> None:
    """
        Draws a rectangle on the canvas
    """
    bbox = [
        [rectangle.corner.x, rectangle.corner.y],
        [rectangle.corner.x+rectangle.height, rectangle.corner.y+rectangle.width]
        ]
    canvas.rectangle(bbox, outline='black', width=2, fill=rectangle.color)


def draw_point(canvas, point) -> None:
    """
        Draws a point on the canvas
    """
    if not hasattr(point, "color"):
        color = 'white'
    else:
        color = point.color
    
    canvas.rectangle([[point.x, point.y], [point.x, point.y]], outline=color, width=1, fill=color)


def draw_circle(canvas, circle) -> None:
    """
        Draws a circle on the canvas
    """

    canvas.circle(circle.center, circle.r, outline=None, fill=circle.color)


def draw_czech_republics_flag(canvas):
    """
        Draws the national flag of Czech Republic on the canvas
    """
    points = [[-150, -100], [0, 0], [150, 0], [150, -100]]
    canvas.polygon(points, fill='red')

    points = [[-150, 100], [150, 100], [150, 0], [0, 0]]
    canvas.polygon(points, fill='white')

    points = [[-150, 100], [0, 0], [-150, -100]]
    canvas.polygon(points, fill='blue')


def draw_ukrainian_flag(canvas):
    """
        Draws the national flag of Ukraine on the canvas
    """
    rectangle_1 = Rectangle()
    rectangle_1.height, rectangle_1.width, rectangle_1.corner = 300, 100, Point()
    rectangle_1.corner.x, rectangle_1.corner.y = -150, -100
    rectangle_1.color = 'yellow'

    rectangle_2 = Rectangle()
    rectangle_2.height, rectangle_2.width, rectangle_2.corner = 300, 100, Point()
    rectangle_2.corner.x, rectangle_2.corner.y = -150, 0
    rectangle_2.color = 'blue'
    draw_rectangle(canvas, rectangle_1)
    draw_rectangle(canvas, rectangle_2)


def main() -> None:
    """
        Main script function.
    """
    world = World()

    canvas = world.ca(width=500, height=500, background='white')

    # Drawind a rectangle
    rectangle = Rectangle()
    rectangle.height, rectangle.width, rectangle.corner = 300, 200, Point()
    rectangle.corner.x, rectangle.corner.y = -150, -100
    rectangle.color = 'green4'

    draw_rectangle(canvas, rectangle)

    # Drawing a circle
    circle = Circle()
    circle.color = 'red'
    circle.r, circle.center = 70, [-25, 0]

    draw_circle(canvas, circle)

    # Drawing a point
    point = Point()
    point.color = 'blue2'
    point.x, point.y = 150, 150

    draw_point(canvas, point)

    # Drawing the national flags
    draw_czech_republics_flag(canvas)
    draw_ukrainian_flag(canvas)

    world.mainloop()


if __name__ == "__main__":
    main()
