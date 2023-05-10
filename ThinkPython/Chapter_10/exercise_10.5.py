def chop(someList: list) -> list:
    someList = someList[1:-1]
    print(someList)
    return None


def main() -> None:
    list_1 = [1, 2, 3, 4, 5]
    chop(list_1)


if __name__ == "__main__":
    main()