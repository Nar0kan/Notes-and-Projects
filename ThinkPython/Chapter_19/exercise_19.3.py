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
        global color, circle
        button_1.configure(state='disabled')
        button_2.configure(state='active')
        circle = canvas.circle([0, 0], 100, fill=colors[randint(0, len(colors)-1)])

    def change_circle_color():
        """
            Changes the circles color
        """
        global color, circle
        color = entry.get()

        if color not in colors:
            color = 'white'
        circle.config(fill=color)

    colors = ['white', 'magenta', 'yellow', 'red', 'cyan', 'blue', 'green']
    canvas = root.ca(width=480, height=480, bg='black')
    button_1 = root.bu(text="Draw the circle", bg='black', fg='green', command=draw_circle)

    entry = root.en(text="Type in color")
    button_2 = root.bu(text="Change color", bg='black', fg='green',\
                        state='disabled', command=change_circle_color)

    root.mainloop()


if __name__ == "__main__":
    main()
