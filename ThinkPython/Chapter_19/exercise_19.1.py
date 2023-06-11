from swampy.Gui import *



def main() -> None:
    """
        The main function in the script.
    """
    root = Gui()
    root.title("Nick Kirichenko")

    def show_label():
        """
            Creates a label
        """
        global button_2

        button_2.configure(state="disabled")
        label = root.la(text="Nice job!")


    def show_button():
        """
            Creates a new button
        """
        global button_2

        button_1.configure(state="disabled")
        button_2 = root.bu(text="Press me now!", command=show_label)

    button_1 = root.bu(text="Press me!", command=show_button)

    root.mainloop()


if __name__ == "__main__":
    main()
