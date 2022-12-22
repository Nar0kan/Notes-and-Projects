# 1) A function object is a value you can assign to
#  a variable or pass as an argument. 
# For example, do_twice is a function that takes a function 
# object as an argument and calls it twice

def do_twice(func) -> None:
    func()
    func()


def print_spam() -> None:
    print("Spam")


do_twice(print_spam)
# Output: 
# Spam
# Spam


# 2)  Modify do_twice so that it takes two arguments, 
# a function object and a value, and calls the
# function twice, passing the value as an argument.

def do_twice(func, value) -> None:
    func(value)
    func(value)


# 3) Write a more general version of print_spam, 
# called print_twice, that takes a string as a
# parameter and prints it twice.

def print_spam(message: str) -> None:
    print(message)


# 4) Use the modified version of do_twice to
# call print_twice twice, passing 'spam' as an argument.

do_twice(print_spam, "Spam2")
# Output:
# Spam2
# Spam2


# 5) Define a new function called do_four that takes
# a function object and a value and calls the
# function four times, passing the value as a parameter. 
# There should be only two statements in
# the body of this function, not four.

def do_four(func, value) -> None:
    do_twice(func, value)
    do_twice(func, value)


do_four(print_spam, "Spam3")
# Output:
# Spam3
# Spam3
# Spam3
# Spam3