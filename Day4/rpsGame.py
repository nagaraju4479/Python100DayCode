import random
#Rock , Paper , Scissors Game

#Rules
#Rock wins aganist Scissors
#Scissor wins aganist paper
#Paper wins aganist Rock

paper = "📄"
rock = "🎸"
scissor = "✂️"

computer_list = [paper,rock,scissor]
user_list = [paper,rock,scissor]

user_selection = int(input("Which one you want to select in [0-2]? Paper[0] , Rock[1] amd Scissor[2] : "))
computer_selection = random.randint(0,2)

# Logic
if user_selection == computer_selection:
    print(f"You selected :\n {user_list[user_selection]} \n Computer Selected : \n {computer_list[computer_selection]}")
    print("It's a Draw")
elif user_selection == 0 and (computer_selection == 1 or computer_selection == 2):
    print(f"You selected :\n {user_list[user_selection]} \n Computer Selected : \n {computer_list[computer_selection]}")
    print("you lose")
elif user_selection == 1 and (computer_selection == 0 or computer_selection == 2):
    print(f"You selected :\n {user_list[user_selection]} \n Computer Selected : \n {computer_list[computer_selection]}")
    print("You win")
elif user_selection == 2 and computer_selection == 0:
    print(f"You selected :\n {user_list[user_selection]} \n Computer Selected : \n {computer_list[computer_selection]}")
    print("You win")
elif user_selection == 2 and computer_selection == 1:
    print(f"You selected :\n {user_list[user_selection]} \n Computer Selected : \n {computer_list[computer_selection]}")
    print("You lose")
elif user_selection >2 or user_selection < 0:
    print("Invalid Entry ! You Lose \n")
    


