def histogram(word: str) -> dict:
    result = dict()

    for letter in word:
        result[letter] = result.get(letter, 0) + 1
    
    return result


def invert_dict(d: dict) -> dict:
    inverted = dict()

    for key in d:
        val = d[key]
        try:
            inverted[val].append(key)
        except KeyError:
            inverted.setdefault(val, [key])
        
    return inverted


def main() -> None:
    h = histogram("entry frag is the important thing for the attack side")
    print(h)
    print(invert_dict(h))
    

if __name__=="__main__":
    main()