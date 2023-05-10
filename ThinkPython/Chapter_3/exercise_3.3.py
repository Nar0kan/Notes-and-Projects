message = 'allen'

def right_justify(value: str) -> None:
    result = ' '*(71-len(value)) + value

    print(result)
    print("Lenght of output (71 because of columns iteration starts at 0): ", len(result))
    print("Last symbol index (column number): ", result.index(result[-1]))


right_justify(message)