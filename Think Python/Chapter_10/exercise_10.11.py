def bisect_left(a, x, lo=0, hi=None, *, key=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    
    if hi is None:
        hi = len(a)
    
    if key is None:
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid
    else:
        while lo < hi:
            mid = (lo + hi) // 2
            if key(a[mid]) < x:
                lo = mid + 1
            else:
                hi = mid
    
    return lo


def bisect_func(someList: list, target):
    t = bisect_left(someList, target)
    return t if t != len(someList) and someList[t] == target else None


def main() -> None:
    list_1 = [0, 1, 1, 1, 1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9]

    print(bisect_func(list_1, 5))
    print(bisect_func(list_1, 4))
    print(bisect_func(list_1, 1))
    print(bisect_func(list_1, -1))


if __name__ == "__main__":
    main()