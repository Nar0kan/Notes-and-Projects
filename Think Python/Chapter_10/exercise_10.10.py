from datetime import datetime


def buildWords_1() -> list:
    words = []

    with open("words.txt", "r") as f:
        for line in f:
            words += [line[:-2]]
    
    return words


def buildWords_2() -> list:
    words = []

    with open("words.txt", "r") as f:
        for line in f:
            words.append(line[:-2])
    
    return words


def main() -> None:
    start = datetime.now()
    buildWords_1()
    end = datetime.now()
    print("+ operator: ", end-start)

    start = datetime.now()
    buildWords_2()
    end = datetime.now()
    print("append method: ", end-start)


if __name__ == "__main__":
    main()