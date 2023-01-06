def print_n_RECURSION(s, n):
    if n <= 0:
        return None
    print(s)
    print_n_RECURSION(s, n-1)


def print_n_LOOP(s, n):
    while n > 0:
        print(s)
        n-=1
    return None


def print_n_FOR(s, n):
    for i in range(0, n):
        print(s)
    return None


def test():
    print_n_RECURSION(3, 6)
    print_n_LOOP(3, 6)
    print_n_FOR(3, 6)


if __name__ == "__main__":
    test()