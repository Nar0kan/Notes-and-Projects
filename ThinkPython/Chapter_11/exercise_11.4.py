def histogram(word: str) -> dict:
    result = dict()

    for letter in word:
        result[letter] = result.get(letter, 0) + 1
    
    return result


def reverse_lookup(d: dict, v) -> list:
    result = []

    for el in d:
        if d[el] == v:
            result.append(el)
    
    return result


def main() -> None:
    h = histogram("entry frag is the important thing for the attack side")
    #print(h)
    print(reverse_lookup(h, 3), "\n", "_"*5)    # ['n', 'h']
    print(reverse_lookup(h, 9), "\n", "_"*5)    # [' ']
    print(reverse_lookup(h, 0))                 # []
    

if __name__=="__main__":
    main()