import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

char_choice = int(input("Enter number of characters in password : "))
num_choice = int(input("Enter number of numbers in password : "))
sym_choice = int(input("Enter number of symbols in password : "))
char_password = ""
num_password = ""
sym_password = ""
password = ""
for char in range(1 , char_choice + 1):
    password += random.choice(letters)
    
for number in range(1 , num_choice + 1):
    password += random.choice(numbers)

for symbol in range(1 , sym_choice + 1):
    password += random.choice(symbols)

print(f"Random password is : {password}")
