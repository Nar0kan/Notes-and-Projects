def remove_duplicates_set(someList: list) -> list:
    return list(set(someList))


def remove_duplicates(someList: list) -> list:
    newList = []

    for i in someList:
        if i not in newList:
            newList.append(i)
    
    return newList


def main() -> None:
    list_1 = [1, 2, 3, 4, 5, 2, 1, 5, "a", "b"]

    print(remove_duplicates_set(list_1))
    print(remove_duplicates_set(list_1+[1, 5, "a", "b", 1, 5, "a", "b"]))

    print(remove_duplicates(list_1))
    print(remove_duplicates(list_1+[1, 5, "a", "b", 1, 5, "a", "b"]))    


if __name__ == "__main__":
    main()