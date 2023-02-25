def cumulative_sum(listOfInt: list) -> list:
    cum_list = []

    for i in range(len(listOfInt)):
        cum_list.append(sum(listOfInt[:i+1]))
    return cum_list
    

def main() -> None:
    list_1 = [1, 2, 3, 4, 5]
    print(cumulative_sum(list_1))

if __name__ == "__main__":
    main()