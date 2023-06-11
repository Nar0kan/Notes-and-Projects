from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageDraw
from canvasvg import *


class Program:
    """
        Represents a program to add elements on the canvas
    """
    extensions = ('png', 'jpg', 'svg', 'ps')

    def __init__(self, root) -> None:
        """ Initializing elements """
        self.root = root
        self.root.update()
        self.setup()


    def setup(self) -> None:
        """
            Draws initial elements on the page (frames, buttons and canvases)
        """
        self.image1 = Image.new("RGB", (1080, 720), (255, 255, 255))
        self.draw = ImageDraw.Draw(self.image1)

        self.elements_frame = Frame(self.root, bg='black')
        self.add_line_button = Button(self.elements_frame, text='Add line', command=self.add_line_window)
        self.add_line_button.grid(column=0, row=1, padx=5)
        self.add_text_button = Button(self.elements_frame, text='Add text', command=self.add_text_window)
        self.add_text_button.grid(column=1, row=1, padx=5)
        self.add_rect_button = Button(self.elements_frame, text='Add rectangle', command=self.add_rect_window)
        self.add_rect_button.grid(column=2, row=1, padx=5)
        self.add_oval_button = Button(self.elements_frame, text='Add oval', command=self.add_oval_window)
        self.add_oval_button.grid(column=3, row=1, padx=5)
        self.add_poly_button = Button(self.elements_frame, text='Add poly', command=self.add_poly_window)
        self.add_poly_button.grid(column=4, row=1, padx=5)

        self.image_canvas = Canvas(self.root, width=1080, height=720, bd=5, bg='white')

        self.save_elements_frame = Frame(self.root, bg='black')
        
        self.save_image_button = Button(self.save_elements_frame, text='Save image', command=self.save_as_image)
        self.filename_label = Label(self.save_elements_frame, text="Filename")
        self.filename_entry = Entry(self.save_elements_frame)

        self.elements_frame.grid(column=0, row=0, columnspan=7, padx=20)
        self.image_canvas.grid(column=2, row=1, padx=20)

        self.save_elements_frame.grid(column=2, row=2, columnspan=7, padx=20)
        self.save_image_button.grid(column=0, row=0)
        self.filename_label.grid(column=1, row=0, columnspan=2)
        self.filename_entry.grid(column=3, row=0, columnspan=3)

        width = 1280
        height = 720
        self.root.geometry(f"{width}x{height}")


    def load_coords_elements(self, window, all: bool=True) -> None:
        """
            Loads entry and label elements for coordinates.
        """
        label = Label(window, text="x0")
        label.grid(row=0, column=0, padx=5, pady=5)
        self.x0_entry = Entry(window)
        self.x0_entry.grid(row=0, column=1, padx=5, pady=5)
        label = Label(window, text="y0")
        label.grid(row=1, column=0, padx=5, pady=5)
        self.y0_entry = Entry(window)
        self.y0_entry.grid(row=1, column=1, padx=5, pady=5)

        if all:
            label = Label(window, text="x1")
            label.grid(row=2, column=0, padx=5, pady=5)
            self.x1_entry = Entry(window)
            self.x1_entry.grid(row=2, column=1, padx=5, pady=5)
            label = Label(window, text="y1")
            label.grid(row=3, column=0, padx=5, pady=5)
            self.y1_entry = Entry(window)
            self.y1_entry.grid(row=3, column=1, padx=5, pady=5)


    def load_coords_values(self, all: bool=True) -> None:
        """
            Gets coordinates from specified entries.
            all - is an easy way to control amount of coordinates gathered.
            By default all=True and there are x0, y0, x1 and y1 coords. If
            all=False: last two elements aren't being retrieved.
        """
        self.x0, self.y0 = int(self.x0_entry.get()), int(self.y0_entry.get())
        if all:
            self.x1, self.y1 = int(self.x1_entry.get()), int(self.y1_entry.get())
        self.color = self.color_entry.get()


    def add_line_window(self) -> None:
        """
            Opens a new window to configure the line that will
            be added on the canvas.
        """
        window = Toplevel(self.root)
        window.title("Add line")

        self.load_coords_elements(window)
        label = Label(window, text="Color")
        label.grid(row=4, column=0, padx=5, pady=5)
        self.color_entry = Entry(window)
        self.color_entry.grid(row=4, column=1, padx=5, pady=5)

        submit = Button(window, text='Submit', command=self.add_line)
        submit.grid(row=5, column=0, columnspan=2, padx=5, pady=5)


    def add_text_window(self) -> None:
        """
            Opens a new window to configure the text that will
            be added on the canvas.
        """
        window = Toplevel(self.root)
        window.title("Add text")

        self.load_coords_elements(window, all=False)
        label = Label(window, text="Text")
        label.grid(row=3, column=0, padx=5, pady=5)
        self.text_entry = Entry(window)
        self.text_entry.grid(row=3, column=1, padx=5, pady=5)
        label = Label(window, text="Color")
        label.grid(row=4, column=0, padx=5, pady=5)
        self.color_entry = Entry(window)
        self.color_entry.grid(row=4, column=1, padx=5, pady=5)

        submit = Button(window, text='Submit', command=self.add_text)
        submit.grid(row=5, column=0, columnspan=2, padx=5, pady=5)


    def add_rect_window(self) -> None:
        """
            Opens a new window to configure the rectangle that will
            be added on the canvas.
        """
        window = Toplevel(self.root)
        window.title("Add rectangle")

        self.load_coords_elements(window)
        label = Label(window, text="Color")
        label.grid(row=4, column=0, padx=5, pady=5)
        self.color_entry = Entry(window)
        self.color_entry.grid(row=4, column=1, padx=5, pady=5)

        submit = Button(window, text='Submit', command=self.add_rect)
        submit.grid(row=5, column=0, columnspan=2, padx=5, pady=5)


    def add_oval_window(self) -> None:
        """
            Opens a new window to configure the oval (ellipse) that will
            be added on the canvas.
        """
        window = Toplevel(self.root)
        window.title("Add oval")

        self.load_coords_elements(window)
        label = Label(window, text="Color")
        label.grid(row=4, column=0, padx=5, pady=5)
        self.color_entry = Entry(window)
        self.color_entry.grid(row=4, column=1, padx=5, pady=5)

        submit = Button(window, text='Submit', command=self.add_oval)
        submit.grid(row=5, column=0, columnspan=2, padx=5, pady=5)


    def add_poly_window(self) -> None:
        """
            Opens a new window to configure the polygon that will
            be added on the canvas.
        """
        window = Toplevel(self.root)
        window.title("Add polygon")

        self.load_coords_elements(window)
        label = Label(window, text="x2")
        label.grid(row=4, column=0, padx=5, pady=5)
        self.x2_entry = Entry(window)
        self.x2_entry.grid(row=4, column=1, padx=5, pady=5)
        label = Label(window, text="y2")
        label.grid(row=5, column=0, padx=5, pady=5)
        self.y2_entry = Entry(window)
        self.y2_entry.grid(row=5, column=1, padx=5, pady=5)
        label = Label(window, text="Color")
        label.grid(row=6, column=0, padx=5, pady=5)
        self.color_entry = Entry(window)
        self.color_entry.grid(row=6, column=1, padx=5, pady=5)

        submit = Button(window, text='Submit', command=self.add_poly)
        submit.grid(row=7, column=0, columnspan=2, padx=5, pady=5)


    def add_line(self):
        """
            Adds the line on the canvas after gathering the entries.
        """
        self.load_coords_values()
        self.image_canvas.create_line([self.x0, self.y0, self.x1, self.y1], fill=self.color)
        self.draw.line([self.x0, self.y0, self.x1, self.y1], self.color)


    def add_text(self):
        """
            Adds the text on the canvas after gathering the entries.
        """
        self.load_coords_values(all=False)
        text = self.text_entry.get()
        self.image_canvas.create_text([self.x0, self.y0], fill=self.color, text=text)
        self.draw.text([self.x0, self.y0], self.color)


    def add_rect(self):
        """
            Adds the rectangle on the canvas after gathering the entries.
        """
        self.load_coords_values()
        self.image_canvas.create_rectangle([self.x0, self.y0, self.x1, self.y1], fill=self.color)
        self.draw.rectangle([self.x0, self.y0, self.x1, self.y1], self.color)


    def add_oval(self):
        """
            Adds the text on the oval (ellipse) after gathering the entries.
        """
        self.load_coords_values()
        self.image_canvas.create_oval([self.x0, self.y0, self.x1, self.y1], fill=self.color)
        try:
            self.draw.ellipse([self.x0, self.y0, self.x1, self.y1], self.color)
        except ValueError:
            self.draw.ellipse([self.x1, self.y1, self.x0, self.y0], self.color)


    def add_poly(self):
        """
            Adds the text on the polygon after gathering the entries.
        """
        self.load_coords_values()
        self.x2, self.y2 = int(self.x2_entry.get()), int(self.y2_entry.get())
        self.image_canvas.create_polygon([self.x0, self.y0, self.x1, self.y1, self.x2, self.y2], fill=self.color)
        self.draw.polygon([self.x0, self.y0, self.x1, self.y1], self.color)


    def has_ext(self) -> bool:
        """
           Checks if self.filename, that must be specified before,
           has a valid extension
        """
        return self.filename.split('.')[-1] in self.extensions


    def save_as_image(self) -> None:
        """
            Saves the self.image_canvas to the file
            self.filename with neccessary extention.
        """
        self.filename = self.filename_entry.get()

        if not self.filename:
            messagebox.showinfo(message="Using default filename 'my_drawing.svg'.")
            self.filename = 'my_drawing.svg'
        elif not self.has_ext():
            self.filename += '.svg'

        file_ext = self.filename.split('.')[-1]
        if file_ext == 'svg':
            saveall(self.filename, self.image_canvas, items=None, margin=10, tounicode=None)
        elif file_ext =='ps':
            self.image_canvas.postscript(file=self.filename, colormode='color')
        elif file_ext in ('png', 'jpg', 'jpeg'):
            self.image1.save(self.filename)
        else:
            messagebox.showerror(message="Cannot save the file with this extention! Must be svg, jpg, png or ps!")


def main() -> None:
    """
        The main funtion in the script.
    """
    root = Tk()
    program = Program(root)
    root.geometry("1140x800")
    root.resizable(0, 0)
    root.mainloop()


if __name__ == "__main__":
    main()
