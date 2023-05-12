def main():
    a = "Some letters"
    print(a)
    print(type(a))

    b = a[:]
    print(b)
    print(type(b))

    print(a == b)
    print(a is b)


if __name__ == "__main__":
    main()