from math import sqrt, pi


def factorial(n: int) -> int:
    return 1 if n == 1 or n == 0 else factorial(n-1)*n


def estimate_pi():
    k = 0
    result = 0
    term = 0

    while result < (10**(-15)):
        term += ((2*sqrt(2)/9801)*(factorial(4*k)*(1103+26390*k)))/((factorial(k)**4)*(396**(4*k)))

        k+=1
        result = 1/term

    return result


def test():
    print(estimate_pi())
    print(abs(estimate_pi()-pi))


if __name__ == "__main__":
    test()