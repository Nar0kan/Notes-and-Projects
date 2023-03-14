from random import random


def sort_by_length(words: list) -> list:
    t = []
    for word in words:
        t.append((len(word), word))
    
    t = sorted(t, reverse=True, key=lambda val: (val[0], random()))

    res = []
    for length, word in t:
        res.append(word)
    
    return res


def main() -> None:
    print(sort_by_length(['Java', 'Python', 'Ruby', 'C++', 'C', 'C#', 'Delphi', 'Pascal', 'JavaScript', 'PHP', 'Go']))


if __name__ == "__main__":
    main()