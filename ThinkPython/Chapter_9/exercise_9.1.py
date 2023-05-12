def main():
    with open("words.txt", "r") as f:
        for i in f:
            j = i.strip("\n")
            if len(j) > 20:
                print(i)



if __name__ == "__main__":
    main()