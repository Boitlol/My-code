
def treasure_island():
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    choice1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()
    if choice1 != "left":
        print("You fell into a hole. Game Over.")
        return

    choice2 = input("You've come to a lake. There is an island in the middle of the lake. "
                    "Type 'wait' to wait for a boat. Type 'swim' to swim across: ").lower()
    if choice2 != "wait":
        print("You got attacked by a trout. Game Over.")
        return


    choice31 = input("You arrive at the island .There is a house with three \n"
                    "One red, one yellow, and one blue. Which color do you choose? ").lower()
    if choice31 == "yellow":
        print("You found the treasure! You Win!")
    elif choice31 == "red":
        print("It's a room full of fire. Game Over.")
    elif choice31 == "blue":
        print("You enter a room of beasts. Game Over.")
    else:
        print("You chose a door that doesn't exist. Game Over.")



treasure_island()