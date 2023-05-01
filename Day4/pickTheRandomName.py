import random
print("Who will pay the bill today \n")
names = input("Enter the names separated by ',' : ")
name_list = names.split(",")
# person_who_will_pay_the_bill = str(random.choice(name_list))
# print(person_who_will_pay_the_bill + " will pay the bill today hahahaha")

print(f"{random.choice(name_list)} will pay the bill today .")