weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height * height)
print("Your BMI is:", bmi)

if bmi < 18.5:
    print("Classification: Underweight")
elif bmi < 25:
    print("Classification: Normal")
elif bmi < 30:
    print("Classification: Overweight")
else:
    print("Classification: Obese")
print()
