print("\nWelcome to the tip calculator.")
total_bill_input = float(input("What was the total bill? $"))
percent_of_tip = int(input(
    "What percentage tip would you like to give? 10, 12 or 15?"))
split_by_people = int(input("How many people to split the bill?"))

percentage = float((percent_of_tip / 100) * total_bill_input)
total_bill = total_bill_input + percentage
total_bill_calculate = total_bill / split_by_people
total_after_split = "{:.2f}".format(total_bill_calculate)
print(f"Each person should pay: ${total_after_split}")
