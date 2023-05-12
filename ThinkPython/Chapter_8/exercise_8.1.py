def displayBackward_1(sequence: str) -> None:
    for i in sequence[::-1]:
        print(i)


def displayBackward_2(sequence: str) -> None:
    print('\n'.join([i for i in sequence[::-1]]))


def displayBackward_3(sequence: str) -> None:
    for i in range(len(sequence)):
        print(sequence[len(sequence)-i-1])


def displayBackward_4(sequence: str) -> None:
    i = len(sequence)-1

    while i >= 0:
        print(sequence[i])
        i-=1


def test():
    displayBackward_1("Awesome")
    displayBackward_2("Cool")
    displayBackward_3("Amazing")
    displayBackward_4("Beautiful")


if __name__ == "__main__":
    test()