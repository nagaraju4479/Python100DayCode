weight = float(input("Enter your weight in Kgs : "))
height = float(input("Enter your Height in Meters : "))

#Calculation
bmi1 = "{:.2f}".format(weight/(height ** 2))
bmi = float(bmi1)

if bmi <= 18.5:
    print(f"Your BMI value is : {bmi} --> Under weight")
elif bmi <= 25:
    print(f"Your BMI value is : {bmi} --> Normal weight")
elif bmi <= 30:
    print(f"Your BMI value is : {bmi} --> Over weght")
elif bmi <= 35:
    print(f"Your BMI value is : {bmi} --> Obesity")
else:
    print(f"Your BMI is : {bmi} --> Obesity in Critical stage")
