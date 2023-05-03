#Sum even numbers 

total = 0
for number in range(1,101):
    if(number % 2 == 0):
        # print(number)
        total+=number
print(f"Sumber of even numbers : {total}")