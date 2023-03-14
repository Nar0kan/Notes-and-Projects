def sumall(counter=0, *args):
    for i in args:
        try:
            counter += i
        except TypeError:
            print(f"'{i}' value is not like the first character type! It won't be summed to the total sum.")
    
    return counter


def main() -> None:
    print(sumall(1, 2, 3, 4, 5, 6, 7))
    print(sumall(1, 2, 'a', 3))
    print(sumall('a'))


if __name__ == "__main__":
    main()