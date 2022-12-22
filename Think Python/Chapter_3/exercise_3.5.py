# 1)  Write a function that draws a grid like the following:
# +----+----+
# |    |    |
# |    |    |
# |    |    |
# |    |    |
# +----+----+
# |    |    |
# |    |    |
# |    |    |
# |    |    |
# +----+----+

def doTwice(func, value) -> None:
    func(value)
    func(value)


def printVal(value: int) -> None:
    print('+----+----+')
    doTwice(print, '|    |    |\n|    |    |')


def draw(value: int=0) -> None:
    doTwice(printVal, 2)
    print('+----+----+')


draw()


# 2) Write a function that draws a similar grid with 
# four rows and four columns.

def doFourth(func, value) -> None:
    doTwice(func, value)
    doTwice(func, value)


def printVal(value: int) -> None:
    print('+----+----+----+----+')
    doTwice(print, '|    |    |    |    |' +\
        '\n' + '|    |    |    |    |')


def draw() -> None:
    doFourth(printVal, 2)
    print('+----+----+----+----+')


draw()
# Output: 
# +----+----+----+----+
# |    |    |    |    |
# |    |    |    |    |
# |    |    |    |    |
# |    |    |    |    |
# +----+----+----+----+
# |    |    |    |    |
# |    |    |    |    |
# |    |    |    |    |
# |    |    |    |    |
# +----+----+----+----+
# |    |    |    |    |
# |    |    |    |    |
# |    |    |    |    |
# |    |    |    |    |
# +----+----+----+----+
# |    |    |    |    |
# |    |    |    |    |
# |    |    |    |    |
# |    |    |    |    |
# +----+----+----+----+