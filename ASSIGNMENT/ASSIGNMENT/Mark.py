mark = float(input("Enter your mark (0-100): "))

    
if 90 <= mark <= 100:
    grade = "A"
elif 80 <= mark < 90:
    grade = "B"
elif 70 <= mark < 80:
    grade = "C"
elif 60 <= mark < 70:
    grade = "D"
elif 0 <= mark < 60:
    grade = "F"
else:
    grade = "Invalid Mark"

   
if grade == "Invalid Mark":
    print(grade)
else:
    print("Grade: " + grade)


