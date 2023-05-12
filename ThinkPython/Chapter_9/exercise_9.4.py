def uses_only(word: str, letters: str) -> bool:
    for i in word:
        if i not in letters:
            return False
        
    return True


def main() -> None:
    check_1 = ["candy", "watermelon", "ballon", "active", "sunset"]
    letters = "anmlobctived"

    for word in check_1:
        print(word, " uses only letters ", letters, " is ", uses_only(word, letters))
    
    check_2 = "hello hell of face fella ace"
    letters = "acefhlo "
    print(check_2, " sentance contains only ", letters, " letters is ", uses_only(check_2, letters))


if __name__ == "__main__":
    main()