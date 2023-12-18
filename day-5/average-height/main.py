# input will be 156 178 165 171 187
student_heights = input("Enter list of number(Example: 156 178 165)\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_heights = 0
for student_height in student_heights:
    total_heights += student_height
print(f"Total height = {total_heights}")

number_of_students = 0
for students in student_heights:
    number_of_students += 1
print(f"Total number of students = {number_of_students}")

average_heights = round(total_heights / number_of_students)
print(f"Average Height: {average_heights}")
