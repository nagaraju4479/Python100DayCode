#Average height without using Sum and Len funcationalities

student_heights = input("Enter student heights : ").split()
total_height = 0
no_of_students = 0
for height in student_heights:
    no_of_students +=1
    total_height += int(height)

print("*******************************")
print(f"Sum of student heights : {total_height}")
print(f"Number of students : {no_of_students}")
average_student_height = round(total_height/no_of_students)
print(f"Average studnets height : {average_student_height}")


