"""I have already been used all of this string methods, 
so will use only recommended one from the book"""

def main():
    message = "Here is the base. We should move on."
    replacedMessage = message.replace("e", "#", 4)
    splitedMessageList = message.split(".")

    print(message)
    print(replacedMessage)

    for sentance in splitedMessageList:
        print(sentance)



if __name__ == "__main__":
    main()