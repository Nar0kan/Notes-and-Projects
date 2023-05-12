def capitalize_all(t: list) -> list:
    res = []
    for s in t:
        res.append(s.capitalize())
    
    return res


def capitalize_nested(nested: list) -> list:
    res = []
    for s in nested:
        res.append(capitalize_all(s))
    
    return res


def main() -> None:
    nested_list = [["fat", "tat", "rat"], ["nut", "cat", "set"], ["map"]]
    print(capitalize_nested(nested_list))


if __name__ == "__main__":
    main()