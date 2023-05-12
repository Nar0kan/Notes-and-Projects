def get_all_rotate_pairs(words: list) -> dict:
    res = dict()
    
    for el in words:
        if el[::-1] in words:
            if el not in res and el[::-1] not in res:
                res[el] = el[::-1]
    
    return res


def main() -> None:
    words = ["alabama", "lullaby", "bypass", "spot", "tops", "was", "saw", "jigsaw", "was", "saw", "was"]

    rotate_pairs = get_all_rotate_pairs(words=words)
    print(rotate_pairs)


if __name__ == "__main__":
    main()