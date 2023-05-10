import random
word_list = ["nagaraju","Madhavi","Ram"]

choice = random.choice(word_list)

guess = input("Enter a letter : ").lower()

print(f"random word is : {choice}")
for letter in choice:
    if letter == guess:
        print(letter)
    else:
        print("*")