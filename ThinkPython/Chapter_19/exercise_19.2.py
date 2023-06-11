from swampy.Gui import *
from random import randint


def main() -> None:
    """
        The main function in the script.
    """
    root = Gui()
    root.title("Nick Kirichenko")

    def draw_circle():
        """
            Draws the circle on a canvas
        """
        canvas.circle([0, 0], 100, fill=colors[randint(0, len(colors)-1)])

    colors = ['white', 'magenta', 'yellow', 'red', 'cyan', 'blue', 'green']
    canvas = root.ca(width=480, height=480, bg='black')
    button_1 = root.bu(text="Draw the circle", bg='black', fg='green', command=draw_circle)

    root.mainloop()


if __name__ == "__main__":
    main()
