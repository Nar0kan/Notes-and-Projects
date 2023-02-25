def is_anagram(str_1: str, str_2: str) -> bool:
    return str_1 == str_2[::-1]


def main() -> None:
    str_1 = "hello"
    str_2 = "olleh"
    str_3 = "hlloe"

    print(is_anagram(str_1, str_2))
    print(is_anagram(str_1, str_3))
    print(is_anagram(str_2, str_3))
    print(is_anagram(str_1, str_1[::-1]))


if __name__ == "__main__":
    main()