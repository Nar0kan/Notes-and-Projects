def computeFactorial(number: int) -> int:
    if not isinstance(number, int) or number < 0:
        raise TypeError("number must be greater or equal to 0 and integer.")
    return 1 if number == 0 else number*computeFactorial(number-1)


if __name__ == "__main__":
    print(computeFactorial(0))
    print(computeFactorial(1))
    print(computeFactorial(2))
    print(computeFactorial(5))
    print(computeFactorial(10))
    # Exceptions:
    #print(computeFactorial("s"))
    #print(computeFactorial(10.2))
    #print(computeFactorial(-2))