from random import randint


def has_duplicates(someList: list) -> bool:
    return True if len(set(someList)) != len(someList) else False


def has_duplicates_list(someList: list) -> bool:
    for el in someList:
        if someList.count(el) > 1:
            return True
    
    return False


def is_birthdayParadox(yourBirthday: int) -> bool:
    birthdayList = []

    for i in range(22):
        birthdayList.append(randint(1, 31))
    
    return yourBirthday in birthdayList


def main() -> None:
    list_1 = [1, 2, 3, 4, 5]

    print(has_duplicates_list(list_1))
    print(has_duplicates_list(list_1+[1, 2]))
    print(has_duplicates_list(list_1+["a"]))

    total, accuracy = 0, 100000
    for i in range(accuracy):
        if is_birthdayParadox(18):
            total += 1
    
    print("Birthday paradox chance is: ", total/accuracy)


if __name__ == "__main__":
    main()