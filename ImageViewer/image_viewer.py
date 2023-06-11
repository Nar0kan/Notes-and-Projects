from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
from os import path, chdir, listdir
from hashlib import md5
from random import randint


class DragManager():
    current_widget = None


    def add_dragable(self, image_viewer, widget, image, images):
        self.widget = widget
        self.image = image
        self.images = images
        self.image_viewer = image_viewer
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)
        widget.configure(cursor="hand2")


    def on_start(self, event):
        widget = event.widget
        widget._drag_start_x = event.x
        widget._drag_start_y = event.y


    def on_drag(self, event):
        widget = event.widget
        x = widget.winfo_x() - widget._drag_start_x + event.x
        y = widget.winfo_y() - widget._drag_start_y + event.y
        widget.place(x=x, y=y)


    def on_drop(self, event):
        x, y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x, y)
        try:
            if ".!canvas" == target.__str__():
                if DragManager.current_widget:
                    DragManager.current_widget.configure(fg='green', bg='white', bd=0)

                ImageViewer.make_image(self.image_viewer, self.image)

                self.widget.grid(column=1, row=self.images.index(self.image)%8, padx=20, pady=5)
                DragManager.current_widget = self.widget
            else:
                self.widget.grid(column=1, row=self.images.index(self.image)%8, padx=20, pady=5)
        except:
            self.widget.grid(column=1, row=self.images.index(self.image)%7, padx=20, pady=5)


class ImageViewer():
    """
        Represents a program to view images in the directory
    """
    def __init__(self, root) -> None:
        self.root = root
        self.setup()


    def setup(self):
        """
            Setup elements
        """
        self.suffixes = ['.png', '.jpg', '.jpeg', '.gif']
        self.directory = 'C:\\Users\\werty\\Pictures'#path.abspath('.') + "\\images"
        self.canvas_size = (720,480)
        self.pages = []
        self.images_labels = {}
        self.current_image = ''
        self.images = self.search_images() + self.search_images('.gif')
        self.show_elements()


    def search_images(self, suffix: str='.jpg') -> list:
        """
            Walks through the self.directory to search
            for all the files with suffix and returns them.
        """
        result=[]

        for name in listdir(self.directory):
            some_file= path.join(self.directory, name)
            if path.isfile(some_file):
                file_suffix = '.' + some_file.split('.')[-1]
                if file_suffix == suffix:
                    result.append(some_file)

        return result


    def load_images_pages(self) -> None:
        """
            Loads the amount of the pages of images found to paginate them.
        """
        self.amount_of_pages = 1
        self.page_num = 1
        self.pages = {}
        self.images_canvases = []

        for i in range(len(self.images)):
            if i%8 == 0:
                self.amount_of_pages += 1

        for page in range(1, self.amount_of_pages):
            self.pages[page] = self.images[int(8*(page-1)):int(page*8)]
        self.current_page = self.pages[self.page_num]

        self.image_canvas = Canvas(self.frame, width=500, height=500,\
                                    bg='#666666', bd=2, scrollregion=(0,0,500,800))
        self.image_canvas.grid(column=3, row=1, padx=5, pady=5)


    def load_images_labels(self) -> None:
        """
            Loads images labels to the canvas with drag and drop functionality.
        """
        for image in self.current_page:
            label = Label(self.image_canvas, text=image.split('\\')[-1])
            label.grid(column=1, row=self.images.index(image)%8, padx=20, pady=5)
            self.images_labels[image] = label
            dnd = DragManager()
            dnd.add_dragable(self, label, image, self.images)

        self.root.update()


    def show_elements(self) -> None:
        """
            Draws initial elements on the page for the user
            to interact with.
        """
        self.dir_label = Label(self.root, text='Current directory: '+self.directory,\
                                font=('Arial', 10))
        self.change_dir_button = Button(self.root, text="Change directory", font=('Arial', 12),\
                                        command=self.change_dir)
        self.canvas = Canvas(self.root, height=480, width=720, bg='black', bd=10, relief='ridge')
        self.open_image = Button(self.root, text='Random image',\
                                font=('Arial', 12), command=lambda:\
                                self.make_image(self.current_page[randint(0, len(self.current_page)-1)]))
        self.next_image_button = Button(self.root, text='>', font=('Arial', 15),\
                                bd=1, fg='yellow', bg='black', command=self.next_image)
        self.prev_image_button = Button(self.root, text='<', font=('Arial', 15),\
                                bd=1, fg='yellow', bg='black', command=self.prev_image)
        self.image_label = Label(self.root, text="Current image: ")

        self.frame = Frame(self.root, width=500,height=500)
        self.frame.grid(column=3, row=2)
        self.next_page_button = Button(self.frame, text='>>', font=('Arial', 15),\
                                bd=1, fg='yellow', bg='black', command=self.next_page)
        self.next_page_button.grid(column=4, row=1, padx=20, pady=5, sticky='w')
        self.prev_page_button = Button(self.frame, text='<<', font=('Arial', 15),\
                                bd=1, fg='yellow', bg='black', command=self.prev_page)
        self.prev_page_button.grid(column=0, row=1, padx=20, pady=5, sticky='e')

        self.change_dir_button.grid(column=0, row=1)
        self.dir_label.grid(column=1, row=1)
        self.canvas.grid(column=1, row=2)
        self.image_label.grid(column=1, row=3)
        self.open_image.grid(column=1, row=4, padx=5, pady=5)
        self.prev_image_button.grid(column=0, row=2, sticky='e')
        self.next_image_button.grid(column=2, row=2, sticky='w')

        self.load_images_pages()
        self.load_images_labels()
        self.make_image(self.images[0])
        self.prev_image_button.configure(state='disabled')

        width = self.frame.winfo_width()+self.canvas_size[0]+200
        height = self.frame.winfo_height()+self.canvas_size[1]
        self.root.geometry(f"{width}x{height}")


    def change_dir(self) -> None:
        """
            Changes the directory.
        """
        self.directory =  filedialog.askdirectory()
        self.dir_label.configure(text=self.directory)
        self.images = self.search_images() + self.search_images('.gif')

        self.images_labels = {}
        self.frame.destroy()
        self.image_canvas.destroy()
        self.frame = Frame(self.root, width=500,height=500)
        self.frame.grid(column=3, row=2)
        self.image_canvas = Canvas(self.frame, width=500, height=500,\
                                    bg='white', bd=2, scrollregion=(0,0,500,800))
        DragManager.current_widget = None
        self.next_page_button = Button(self.frame, text='>>', font=('Arial', 15),\
                                bd=1, fg='yellow', bg='black', command=self.next_page)
        self.next_page_button.grid(column=4, row=4, padx=20, pady=5, sticky='w')
        self.prev_page_button = Button(self.frame, text='<<', font=('Arial', 15),\
                                bd=1, fg='yellow', bg='black', command=self.prev_page)
        self.prev_page_button.grid(column=0, row=4, padx=20, pady=5, sticky='e')
        self.prev_page_button.configure(state='disabled')

        self.load_images_pages()
        self.load_images_labels()
        self.make_image(self.images[0])

        self.prev_image_button.configure(state='disabled')
        self.next_image_button.configure(state='normal')

        width = self.frame.winfo_width()+self.canvas_size[0]+200
        height = self.frame.winfo_height()+self.canvas_size[1]
        self.root.geometry(f"{width}x{height}")


    def make_image(self, image) -> None:
        """
            Creates an image instance based on the 'image'
            parameter. Draws it on the canvas after resize proccess.
        """
        self.current_image = image
        self.next_image_button.configure(state='normal')
        self.prev_image_button.configure(state='normal')

        try:
            self.pilImage = Image.open(self.current_image)
            resized_image=self.pilImage.resize(self.canvas_size, Image.LANCZOS)
            self.img = ImageTk.PhotoImage(resized_image)
            self.canvas.delete(ALL)
            self.canvas.create_image(self.canvas_size[0]/2+10, self.canvas_size[1]/2+10,\
                                      anchor=CENTER,image=self.img)
            self.image_label['text']='Current Image: '+ self.current_image.split('\\')[-1]

            cur = self.images.index(self.current_image)
            if cur == len(self.images)-1:
                self.next_image_button.configure(state='disabled')
            elif cur == 0:
                self.prev_image_button.configure(state='disabled')

            if DragManager.current_widget:
                DragManager.current_widget.configure(fg='green', bg='white')
            self.images_labels[self.current_image].configure(fg='magenta', bg='black', bd=2)
            DragManager.current_widget = self.images_labels[self.current_image]
        except TypeError:
            messagebox.showerror('Error!','File type is unsupported.')


    def next_image(self) -> None:
        """
            Draws the next image on the canvas
        """
        try:
            cur = self.images.index(self.current_image)
            if cur == len(self.images)-2:
                self.next_image_button.configure(state='disabled')
                self.make_image(self.images[-1])
            else:
                if cur%8==7:
                    self.next_page()
                self.make_image(self.images[cur+1])
            self.prev_image_button.configure(state='normal')
        except KeyError:
            self.next_page()
            self.images_labels[self.current_image].configure(fg='magenta', bg='black', bd=2)
            DragManager.current_widget = self.images_labels[self.current_image]


    def prev_image(self) -> None:
        """
            Draws the previous image on the canvas
        """
        try:
            cur = self.images.index(self.current_image)
            if cur == 1:
                self.prev_image_button.configure(state='disabled')
                self.make_image(self.images[0])
            else:
                if cur%8==0:
                    self.prev_page()
                self.make_image(self.images[cur-1])
            self.next_image_button.configure(state='normal')
        except KeyError:
            self.prev_page()
            self.images_labels[self.current_image].configure(fg='magenta', bg='black', bd=2)
            DragManager.current_widget = self.images_labels[self.current_image]


    def next_page(self) -> None:
        """
            Goes to the next page in the self.pages to load
            the next elements in the images lists.
        """
        DragManager.current_widget = None
        self.prev_page_button.configure(state='normal')

        if self.page_num + 1 < self.amount_of_pages:
            self.page_num += 1
            self.current_page = self.pages[self.page_num]
        if self.page_num + 1 == self.amount_of_pages:
            self.next_page_button.configure(state='disabled')

        self.image_canvas.destroy()
        self.image_canvas = Canvas(self.frame, width=500, height=500,\
                                    bg='#666666', bd=2, scrollregion=(0,0,500,800))
        self.image_canvas.grid(column=3, row=1, padx=5, pady=5)
        self.load_images_labels()

        width = self.frame.winfo_width()+self.canvas_size[0]+200
        height = self.frame.winfo_height()+self.canvas_size[1]
        self.root.geometry(f"{width}x{height}")


    def prev_page(self) -> None:
        """
            Goes to the previous page in the self.pages to load
            the previous elements in the images lists.
        """
        DragManager.current_widget = None
        self.next_page_button.configure(state='normal')

        if self.page_num > 1:
            self.page_num -= 1
            self.current_page = self.pages[self.page_num]
        if self.page_num == 1:
            self.prev_page_button.configure(state='disabled')

        self.image_canvas.destroy()
        self.image_canvas = Canvas(self.frame, width=500, height=500,\
                                   bg='#666666', bd=2, scrollregion=(0,0,500,800))
        self.image_canvas.grid(column=3, row=1, padx=5, pady=5)
        self.load_images_labels()

        width = self.frame.winfo_width()+self.canvas_size[0]+200
        height = self.frame.winfo_height()+self.canvas_size[1]
        self.root.geometry(f"{width}x{height}")


def main() -> None:
    """
        The main function in the script.
    """
    root = Tk()
    root.title("Image viewer")
    root.geometry("1480x620")
    GUI = ImageViewer(root)
    root.resizable(False,False)
    root.mainloop()


if __name__ == "__main__":
    main()
