weight = float(input("Enter your weight in Kgs : "))
height = float(input("Enter your height in meters : "))

#BMI calculation

bmi1 = weight / (height * height)
bmi=round(bmi1,2)
print("******************************\n")

print("Your BMI value is : "+str(bmi))
if bmi<= 18.4:
    print("You are under weight , please eat more Fat items !")
elif bmi>= 18.5 and bmi<=24.9:
    print("You are Normal weight - Congratulations!")
elif bmi >=25 and bmi <= 39.9:
    print("You are over weight - do proper deit and Exercises regulerly!")
else:
    print("You are Obesity , please contact your nutrition and reduce weight")