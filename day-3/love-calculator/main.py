print("\nWelcome to Love Calculator\n")
name1 = input("Enter Your Name: ")
name2 = input("Enter Your Lover Name: ")

combine_name = name1 + name2
T = combine_name.lower().count('t')
R = combine_name.lower().count('r')
U = combine_name.lower().count('u')
E = combine_name.lower().count('e')
first_number = T + R + U + E

L = combine_name.lower().count('l')
O = combine_name.lower().count('o')
V = combine_name.lower().count('v')
E = combine_name.lower().count('e')
second_number = L + O + V + E
love_score = int(str(first_number) + str(second_number))

if (love_score < 10 or love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40 and love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
