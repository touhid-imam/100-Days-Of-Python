# input will be like 78 65 89 86 55 91 64 89
student_scores = input("Input Score List: \n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Find Highest score from an array
max_score = 0
for high_score in student_scores:
    if high_score > max_score:
        max_score = high_score

# print(f"Highest score is: {max_score}")

for number in range(1, 10):
    print(number)
