def customDivmod(div: int, num: int) -> tuple():
    quot = 0
    
    while div>=num:
        quot+=1
        div=div-num
    
    rem = div
    return quot, rem
    

def main() -> None:
    quot, rem = customDivmod(7, 3)
    print(quot, " | ", rem)    


if __name__ == "__main__":
    main()