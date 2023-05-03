#Get Highest and lowest scores in the list with out using "min " and "Max" functions

student_scores = input("Enter student scores  : ").split()

highest_score = 0

for n in range(0,len(student_scores)):
    student_scores[n]=int(student_scores[n])
      
print("******************************")            
print(f"student scores in the : {student_scores}")

for score in student_scores:
    score > highest_score
    highest_score = score
print(f"Highest score : {highest_score}")
