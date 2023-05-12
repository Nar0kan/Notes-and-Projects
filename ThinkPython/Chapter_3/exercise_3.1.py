try:
    repeat_lyrics()
except NameError:
    print("repeat_lyrics must be identified before it is used. Name error appeared.")

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")


def repeat_lyrics():
    print_lyrics()
    print_lyrics()