def is_palindrome(sequence: str) -> bool:
    return True if sequence == sequence[::-1] else False


if __name__ == "__main__":
    print(is_palindrome("aboba"))
    print(is_palindrome("Manage"))