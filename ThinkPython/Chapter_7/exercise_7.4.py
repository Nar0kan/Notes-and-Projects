def eval_loop() -> None:
    while True:
        option = input("> ")

        if option == 'done':
            break
        
        result = eval(option)
        print(result)
    
    return result


if __name__ == "__main__":
    eval_loop()