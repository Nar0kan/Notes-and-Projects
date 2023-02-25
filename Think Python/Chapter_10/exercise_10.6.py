def is_sorted(someList: list) -> bool:
    for i in range(len(someList)-1):
        if type(someList[i]) == type(someList[i+1]):
            if someList[i] > someList[i+1]:
                return False
        else:
            raise ValueError("Elements in 'someList' should be either only strings or only integers!")
    
    return True


def main() -> None:
    list_1 = [1, 2, 3, 4, 5]

    print(is_sorted(list_1))
    print(is_sorted(list_1+[4]))
    print(is_sorted(["a", "b", "c"]))
    print(is_sorted(["a", "b", "a"]))


if __name__ == "__main__":
    main()