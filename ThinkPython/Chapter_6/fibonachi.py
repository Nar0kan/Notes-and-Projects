def computeFibonachi(number: int) -> int:
    return number if number == 0 or number == 1 else (computeFibonachi(number-1) + computeFibonachi(number-2))


if __name__ == "__main__":
    print(computeFibonachi(10))
    print(computeFibonachi(11))
    print(computeFibonachi(1))
    print(computeFibonachi(0))
    print(computeFibonachi(20))