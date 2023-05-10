def has_duplicates(someList: list) -> bool:
    memo = dict()

    for i in someList:
        if i in memo:
            return True
        memo[i] = 0

    return False


def main() -> None:
    someList = ['a', 'b', 'c', 'a']
    print(has_duplicates(someList))

    someList = ['a', 'b', 'c', 'd', 'e']
    print(has_duplicates(someList))


if __name__ == "__main__":
    main()