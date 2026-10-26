
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

choice1 = input("Left or right? ").lower()

if choice1 == "left":
    choice2 = input("Swim or wait? ").lower()

    if choice2 == "wait":
        choice3 = input("Choose a door: red, blue or yellow: ").lower()

        if choice3 == "yellow":
            print("You found the treasure!")
        elif choice3 == "red":
            print("You entered a room of fire. Game over!")
        elif choice3 == "blue":
            print("A dragon ate you. Game over!")
        else:
            print("Invalid door. Game over!")
    else:
        print("A crocodile attacked you. Game over!")
else:
    print("You fell into a hole. Game over!")
