from datetime import datetime

def main() -> None:
    words = dict()

    with open("words.txt", "r") as f:
        for line in f:
            word = line.split("\n")[0]
            words[word] = 0

    start = datetime.now()
    vagrant = 'vagrant' in words
    timeResult = datetime.now()-start
    print("Total time in microseconds: ", timeResult.microseconds)

if __name__=="__main__":
    main()