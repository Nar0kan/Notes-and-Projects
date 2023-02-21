def main() -> None:
    for k in range(18, 100):
        j = k
        i = 0
        count = 0
        ageList = []

        while j < 125:
            if len(str(i)) == len(str(j)):
                if str(i) == str(j)[::-1]:
                    count += 1
                    ageList.append((str(i), str(j)))
            else:
                if '0'+str(i) == str(j)[::-1]:
                    count += 1
                    ageList.append(('0'+str(i), str(j)))
            j += 1
            i += 1
        
        if count >= 8: 
            print(ageList)
            # He is 57 y.o. 


if __name__ == "__main__":
    main()