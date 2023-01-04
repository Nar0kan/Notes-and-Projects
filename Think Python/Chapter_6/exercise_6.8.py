def gcdBased(a: int, b: int) -> int:
    if a > b:
        for i in range(2, b):
            if a % i and b % i:
                return i
    elif a < b:
        for i in range(2, a):
            if a % i and b % i:
                return i
    elif a == b:
        return a
    else:
        return 1


def gcd(a: int, b: int) -> int:
    if a == b:
        return a
    elif a < b:
        return gcd(b, a)
    else:
        return gcd(b, a-b)


if __name__ == "__main__":
    print(gcd(16, 24))
    print(gcd(16, 16))
    print(gcd(24, 16))