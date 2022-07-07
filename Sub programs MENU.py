def player1Game():
    print("1 player game chosen")

def player2Game():
    print("2 player game chosen")

def online():
    print("Online game chosen")

def menu():
    print("Press 1 for 1 player game >>> ")
    print("Press 2 for 2 player game >>> ")
    print("Press 3 for online >>> ")
    print("Press 1 to exit >>> ")

    userInput = int(input("Enter 1,2,3 or 4 >>> "))

    if userInput == 1:
        player1Game()
    elif userInput == 2:
        player2Game()
    elif userInput == 3:
       online()
    elif userInput == 4:
        print("Exiting...")
    else:
        print("input invalid")     
        menu()



menu()
