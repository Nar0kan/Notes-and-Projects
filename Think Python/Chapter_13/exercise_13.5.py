from random import choice


def histogram(values: str) -> dict:
    result = {}

    for value in values.lower():
        if value not in result:
            result[value] = 1
        else:
            result[value] += 1

    return result


def choose_from_hist(hist: dict) -> str:
    return choice(''.join([key*val for key, val in hist.items()]))


def main() -> None:
    phrase = "My name is Nikita and I'm a gamer!"

    hist = histogram(phrase)
    #print(hist)
    result = {}

    for i in range(100000):
        random_value = choose_from_hist(hist)
        prob =  hist[random_value] / len(phrase)

        if random_value not in result.keys():
            result[random_value] = 1
        else:
            result[random_value] += 1
    
    for key, val in hist.items():
        print(key, hist[key] / len(phrase))

    print('\n\n')

    for key, val in result.items():
        print(key, result[key] / 100000)


if __name__=="__main__":
    main()
