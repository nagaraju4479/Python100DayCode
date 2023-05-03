#Find the Average height of the students

student_heights = input("Enter student heights separated by ','  : ").split()

for height in range(0,len(student_heights)):
    student_heights[height]=int(student_heights[height])
print(student_heights)

sum_student_heights = sum(student_heights)
total_number_of_student = len(student_heights)
average_height = round(sum_student_heights / total_number_of_student)
print("************************* \n")
print(f"Total number of student : {total_number_of_student}")
print(f"Average of student heights : {average_height}")