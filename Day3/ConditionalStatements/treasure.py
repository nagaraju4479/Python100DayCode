print("Welcome to the Treasure Island! Your mission is to find the Treasure\n")
choice = input("You come to Cross road , Choose right or left : ").lower()

#Logic
if choice == "right":
    choice2 = input("You come to Island , will you 'Wait' for the Boat or 'Swim' accross the water ? ").lower()
    if choice2 == "wait":
         choice3 = input("Great choice , You have reached the Island , there are 3 Boxes are there 'Red','Green' and 'Yellow' choose right one and get the Treasure : ").lower()
         if choice3 == 'yellow':
             print("Congratulation, you got the Treasure.")
         else:
             print("Game Over!")
    else:
        print("Game Over!")
    
else:
    print("Game over!")

