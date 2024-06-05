def welcome ():
    print("Welcome to the Treasure Island.\nYour mission is to find the treasure.")
    direction = input("Left or right?\n")

    def gameOver():
        print("Game Over")

    if direction.lower() == "right":
        gameOver()
        

    elif direction.lower() == "left":
        action = input("Swim or wait?\n")

        if action.lower() == "swim":
            gameOver()
        elif action.lower() == "wait":
            door = input("Which door?\n")

            if (door.lower() == "blue") or (door.lower() == "red"):
                gameOver()

            elif door.lower() == "yellow":
                print ("You Win!\n")

        else:
            print("Wrong input, please try again!")
            quit = input("Press 'Q' to quit, or press any key to restart the game!\n")

            if quit.lower() != "q":
                welcome()
            else:
                print("See you again next time!\n")

    else:
        welcome()

welcome() 