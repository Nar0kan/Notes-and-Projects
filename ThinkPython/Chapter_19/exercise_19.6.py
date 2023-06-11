from tkinter import *
from tkinter import messagebox
from tkhtmlview import HTMLLabel
import urllib.request
from urllib.error import URLError
from googlesearch import search


class ResizingCanvas(Canvas):
    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        self.config(width=self.width, height=self.height)
        self.scale("all", 0, 0, wscale,hscale)


class Browser:
    """
        Represents a browser
    """
    def __init__(self, root) -> None:
       self.root = root
       self.filename = "file.txt"
       self.setup()
    

    def setup(self) -> None:
        """
            Setups frame, canvas and elements on the browser
        """
        self.frame = Frame(self.root, bg='pink')
        self.url_entry = Entry(self.frame, width=100)
        self.load_page_button = Button(self.frame, text='Load page', command=self.load_page)
        self.canvas = ResizingCanvas(self.root, bd=5, bg='#141414')

        self.my_label = HTMLLabel(self.canvas, html="""
            <ul>
                <li><a href='https://github.com/Nar0kan' target="_blank">Github</a></li>
                <li><a href='https://www.linkedin.com/in/nikita-kirichenko-781062251/' target="_blank">Linkedin</a></li>
                <li><a href='mailto:nick.kirichenko.dev@gmail.com' target="_blank">Gmail</a></li>
            </ul>
            """, bg='#141414', fg="white")

        self.frame.pack(padx=10)
        self.url_entry.grid(column=0, row=0, columnspan=3)
        self.load_page_button.grid(column=3, row=0, columnspan=2, padx=2)
        self.canvas.pack(fill=BOTH, expand=True)
        self.my_label.pack(fill=BOTH, expand=True)


    def load_page(self) -> None:
        """
            Loads the page data on the canvas using urllib and HTMLLabel
        """
        self.url = self.url_entry.get()
        if not self.url:
            messagebox.showerror(message="Please, specify the url before loading the page!")

        try:
            self.load_file()
        except (URLError, ValueError) as e:
            messagebox.showerror(message="URL is invalid! please, try another one!")
            return None

        self.canvas.destroy()
        self.my_label.destroy()
        self.root.update()
        self.canvas = ResizingCanvas(self.root, bd=5, bg='#141414')
        self.canvas.pack(fill=BOTH, expand=True)
        self.my_label = HTMLLabel(self.canvas, html=self.file_text, bg='#141414', fg="white")
        self.my_label.pack(fill=BOTH, expand=True)


    def load_file(self) -> None:
        """
            Loads the page data in the self.file_text variable
        """
        fp = urllib.request.urlopen(self.url)
        mybytes = fp.read()
        self.file_text = mybytes.decode("utf8")
        fp.close()


def main() -> None:
    """
        The main funtion in the script.
    """
    root = Tk()
    program = Browser(root)
    root.geometry("1280x720")
    root.mainloop()


if __name__ == "__main__":
    main()
