# here the line is like line = ["a", "b", "c"] so we need to put X
line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?
# 🚨 Don't change the code ab 

find_row = position[0].lower()
abc = ["a", "b", "c"]
row_index = abc.index(find_row)
x_position = int(position[1]) - 1
map[x_position][row_index] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
