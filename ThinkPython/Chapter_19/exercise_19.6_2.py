import tkinter as tk
from tkinter import ttk
from html.parser import HTMLParser
from urllib.request import urlopen
import urllib.request
from urllib.parse import urlencode, quote_plus


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.text = ""
        self.tag_stack = []

    def handle_starttag(self, tag, attrs):
        self.tag_stack.append(tag)
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.links.append(attr[1])

    def handle_endtag(self, tag):
        self.tag_stack.pop()

    def handle_data(self, data):
        if self.tag_stack:
            if self.tag_stack[-1] in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'a'):
                self.text += data

    def handle_startendtag(self, tag, attrs):
        if tag == 'img':
            for attr in attrs:
                if attr[0] == 'src':
                    self.text += f"[Image: {attr[1]}]"


def search_button_clicked():
    query = url_entry.get()

    if is_valid_url(query):
        handle_url_search(query)
    else:
        handle_text_search(query)


def is_valid_url(url):
    # Simple check for valid URL format
    return url.startswith("http://") or url.startswith("https://")


def handle_url_search(url):
    response = urlopen(url)
    html_data = response.read().decode('utf-8')

    parser = MyHTMLParser()
    parser.feed(html_data)

    # Clear canvas
    canvas.delete('all')

    # Draw parsed text on canvas
    canvas.create_text(10, 10, anchor='nw', text=parser.text, width=canvas.winfo_width()-20)

    response.close()


def handle_text_search(text):
    query = urllib.parse.urlencode({'q': text}, quote_via=urllib.parse.quote_plus)
    search_url = f"https://www.google.com/search?{query}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    req = urllib.request.Request(search_url, headers=headers)

    try:
        response = urllib.request.urlopen(req)
        html_data = response.read().decode('utf-8')

        parser = MyHTMLParser()
        parser.feed(html_data)

        # Clear canvas
        canvas.delete('all')

        # Draw links on canvas
        for i, link in enumerate(parser.links):
            canvas.create_text(10, 30 + i * 20, anchor='w', text=link)

        response.close()
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")


root = tk.Tk()
root.title("Simple Browser")

# URL Entry and Search Button
url_entry = ttk.Entry(root)
url_entry.pack(fill='x', padx=10, pady=10)

search_button = ttk.Button(root, text="Search", command=search_button_clicked)
search_button.pack(padx=10, pady=5)

# Canvas for displaying parsed text or links
canvas = tk.Canvas(root)
canvas.pack(fill='both', expand=True)

# Resize canvas when the window is resized
root.bind("<Configure>", lambda event: canvas.configure(width=event.width, height=event.height))

root.mainloop()
