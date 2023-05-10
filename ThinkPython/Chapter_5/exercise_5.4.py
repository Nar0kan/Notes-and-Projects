def is_triangle(a: int, b: int, c: int) -> bool:
    if a+b <= c or a+c <=b or b+c <= a:
        print("No")
        return False
    else:
        print("Yes")
        return True


a = int(input("Input first stick length: "))
b = int(input("Input second stick length: "))
c = int(input("Input third stick length: "))
is_triangle(a, b, c)