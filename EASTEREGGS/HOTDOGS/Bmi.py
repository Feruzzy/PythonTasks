weight = float(input("Enter weight in pounds: "))
height = float(input("Enter height in inches: "))

weight_in_kg = weight * 0.45359237
meters = height * 0.0254

bmi = weight_in_kg / (meters ** 2)
print("BMI:", bmi)
