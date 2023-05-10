def nested_sum(listOfInt: list) -> int:
    return sum(listOfInt)


def nested_loop_sum(listOfInt: list) -> int:
    total = 0

    for i in listOfInt:
        total += i
    
    return total


def main() -> None:
    list_1 = [1, 2, 3, 4, 5]

    print(nested_sum(list_1))               # 15
    print(nested_loop_sum(list_1+list_1))   # 30


if __name__ == "__main__":
    main()