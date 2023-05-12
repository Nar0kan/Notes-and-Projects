from datetime import datetime


def fibonacci(num: int) -> int:
    if num == 1:
        return 1
    elif num == 0:
        return 0
    return fibonacci(num-1) + fibonacci(num-2)


def fibonacciMemo(num: int, known={0:0, 1:1}) -> int:
    if num in known:
        return num
    
    res = fibonacci(num-1) + fibonacci(num-2)
    known[num] = res
    return res


def main() -> None:
    start = datetime.now()
    a = fibonacci(16)
    total = datetime.now() - start
    print(a, "\nTotal time for fibonacci 16: ", total.microseconds)

    start2 = datetime.now()
    b = fibonacciMemo(16)
    total2 = datetime.now() - start2
    print(b, "\nTotal time for fibonacci with memo 16: ", total2.microseconds)

    start3 = datetime.now()
    c = fibonacci(21)
    total3 = datetime.now() - start3
    print(c, "\nTotal time for fibonacci 21: ", total3.microseconds)

    start4 = datetime.now()
    d = fibonacciMemo(21)
    total4 = datetime.now() - start4
    print(d, "\nTotal time for fibonacci with memo 21: ", total4.microseconds)

    # My results
    #Total time for fibonacci 16:  997
    #Total time for fibonacci with memo 16:  2004
    #Total time for fibonacci 21:  8000
    #Total time for fibonacci with memo 21:  7006
    

if __name__=="__main__":
    main()