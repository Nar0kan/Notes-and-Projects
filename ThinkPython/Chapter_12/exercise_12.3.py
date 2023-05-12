def most_freequent(s: str, outprintSort: bool=False) -> str:
    low = s.lower()
    d = dict()

    for i in low:
        d[i] = d.get(i, 0) + 1
    
    low = sorted(d, reverse=True, key=lambda key: d[key])

    if outprintSort:
        res = ""

        for i in low:
            for j in range(d[i]):
                res+=i
            
        return res
    else:
        return [(i, d[i]) for i in low]


def main() -> None:
    print(most_freequent("Can you hear the silence? Can you see the dark? Can you fix up broken... Can you feel my heart?"))


if __name__ == "__main__":
    main()