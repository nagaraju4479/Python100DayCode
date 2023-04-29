current_age = int(input("Enter your current Age in Years : "))
target_age_years = 90

year = 1
days = 365
week = 52
month = 12

#Calculation
year_left = target_age_years - current_age
days_left = year_left * days
weeks_left = year_left * week
months_left = year_left * month

#Final Result
print("*******************************\n\n")
print(f"Hear is your remaining life time: \n Years : {year_left} \n Months: {months_left}  \n Weeks : {weeks_left}\n Days  : {days_left} ")


