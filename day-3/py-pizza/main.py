print("\nWelcome to Python Pizza Deliveries!\n")
print("Pizza Size: Large-L, Medium-M, Small-S \nAdd Pepperoni or extra_cheese: Yes-Y, No-N")
size = input("Enter the Pizza Size:  ")
add_pepperoni = input("Do you like to add pepperoni? ")
extra_cheese = input("Do you like to add Extra Cheese?")

bill = 0
if (size == "S"):
    bill += 15
elif (size == "M"):
    bill += 20
else:
    bill += 25

if (size == "S" and add_pepperoni == "Y"):
    bill += 2
if (size in ("M", "L") and add_pepperoni == "Y"):
    bill += 3
if (extra_cheese == "Y"):
    bill += 1

print(f"Your Final Bill is: ${bill}")
