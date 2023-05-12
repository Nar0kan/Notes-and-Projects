def middle(someList: list) -> list:
    newList = someList[1:]  # forget first element
    newList.pop()           # pop last element
    return newList


def main() -> None:
    list_1 = [1, 2, 3, 4, 5]
    print(middle(list_1))


if __name__ == "__main__":
    main()