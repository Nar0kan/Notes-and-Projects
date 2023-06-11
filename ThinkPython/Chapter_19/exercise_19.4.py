from swampy.Gui import *
from PIL import Image, ImageTk


def main() -> None:
    """
        The main function in the script.
    """
    root = Gui()
    root.title("Image viewer")

    canvas = root.ca(width=320)
    photo = ImageTk.PhotoImage(file="images/pexels-brett-sayles-992734.jpg", width=30, height=10)
    button_photo = ImageTk.PhotoImage(file="images/pexels-jakub-novacek-924824.jpg", width=32, height=18)
    label_photo = ImageTk.PhotoImage(file="images/pexels-krivec-ales-547115.jpg", width=32, height=18)

    button = root.bu(image=button_photo, fg='white', text='Button')
    label = root.la(text="Label", image=label_photo)
    canvas.image([0, 0], image=photo)

    root.mainloop()


if __name__ == "__main__":
    main()
