def is_palindrome(text: str) -> bool:
    if len(text) <=1:
        return True
    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    
    return False


def main() -> None:
    print(is_palindrome("ava"))
    print(is_palindrome("avva"))
    print(is_palindrome("avca"))
    
    numbers = []
    i = 0

    for i in range(1000000):
        if len(str(i)) < 6:
            k = 6 - len(str(i))
            numbers.append(str(k*"0" + str(i)))
        else:
            numbers.append(str(i))

    for num in numbers:
        if is_palindrome(num): # last check
            prenum = int(num) - 1
            if len(str(prenum)) < 6:   
                k = int(6 - len(str(prenum)))
                prenum = str(k*"0" + str(prenum))
            
            
            if is_palindrome(str(prenum)[1:-1]):     # middle 4
                preprenum = int(prenum) - 1
                if len(str(preprenum)) < 6:
                    k = 6 - len(str(preprenum))
                    preprenum = str(k*"0" + str(preprenum))
                
                if is_palindrome(str(preprenum)[1:]):    # last 5
                    prepreprenum = int(preprenum) - 1
                    if len(str(prepreprenum)) < 6:
                        k = 6 - len(str(prepreprenum))
                        prepreprenum = str(k*"0" + str(prepreprenum))
                    
                    if is_palindrome(str(prepreprenum)[2:]):    # last 4
                        preprepreprenum = int(prepreprenum) - 1
                        if len(str(preprepreprenum)) < 6:
                            k = 6 - len(str(preprepreprenum))
                            preprepreprenum = str(k*"0" + str(preprepreprenum))
                        
                        print(prepreprenum)


if __name__ == "__main__":
    main()