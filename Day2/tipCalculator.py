bill_amount = float(input("Enter your bill amount : "))
tip_in_percentage = int(input("What percentage you want give as a Tip --> 10 , 12, 15 ,20 ...? "))
people_to_share = int(input("Enter number of people to share the amount : "))

#Calculation
tip_amount = (tip_in_percentage/bill_amount)* 100
total_bill = bill_amount + tip_amount
individual_share = total_bill / people_to_share

print("*************************\n")
print(f"Total bill amount : {round(total_bill,2)}")
print(f"Share per person : {round(individual_share,2)}")
