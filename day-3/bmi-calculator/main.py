height = float(input("Input your height: "))
weight = int(input("Input your weight: "))

bmi_measure = weight / height ** 2
if bmi_measure <= 18.5:
    print(f"Your BMI is {bmi_measure}, you are underweight.")
elif bmi_measure < 25:
    print(f"Your BMI is {bmi_measure}, you have a normal weight.")
elif bmi_measure < 30:
    print(f"Your BMI is {bmi_measure}, you are slightly overweight.")
elif bmi_measure < 35:
    print(f"Your BMI is {bmi_measure}, you are obese.")
elif bmi_measure >= 35:
    print(f"Your BMI is {bmi_measure}, you are clinically obese.")
else:
    print("Invalid BMI")
