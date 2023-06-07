from vpython import *


def task_1() -> None:
    """
        Draws a blue sphere in specified position.
    """
    canvas(width=1200, height=800)

    sphere_color = vector(0,0,1)
    sphere_center = vector(128, 128, 128)
    sphere(pos=sphere_center, radius=128, color=sphere_color)


def task_2() -> None:
    """
        Draws a cube of spheres with defined RGB colors
        taken from their position values
    """
    step = range(0, 256, 51)

    for x in step:
        for y in step:
            for z in step:
                sphere_center = vector(x, y, z)
                sphere_color = vector(x/256, y/256, z/256)
                sphere(pos=sphere_center, radius=128, color=sphere_color)


def task_3() -> None:
    """
        Draws a cube of spheres with all defined RGB colors
        taken from their position values
    """
    step = range(0, 256, 1)

    for x in step:
        for y in step:
            for z in step:
                sphere_center = vector(x, y, z)
                sphere_color = vector(x/256, y/256, z/256)
                sphere(pos=sphere_center, radius=128, color=sphere_color)


def main():
    """
        The main function in the script.
    """
    task_1()
    task_2()
    task_3()

    while True:
        rate(30)


if __name__ == '__main__':
    main()
