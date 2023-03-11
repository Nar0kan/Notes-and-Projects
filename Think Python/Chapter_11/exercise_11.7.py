def ack(m: int, n: int, memo={0: 1}) -> int:
    """
    Evaluate Ackermann's function
    """
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))


def ackMemo(m: int, n: int, memo={}) -> int:
    """
    Evaluate Ackermann's function
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackMemo(m-1, 1)
    
    if (m, n) in memo:
        return memo[(m, n)]
    else:
        memo[(m, n)] = ackMemo(m-1, ackMemo(m, n-1))
        return memo[(m, n)]


if __name__ == "__main__":
    print(ack(3, 4))
    print(ackMemo(3, 8))