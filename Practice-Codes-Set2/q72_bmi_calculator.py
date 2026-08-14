# Q72. Body Mass Index (BMI) Calculator

height = 1.72
weight = 70
bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Height          : {height} m")
print(f"Weight          : {weight} kg")
print(f"BMI             : {bmi:.2f}")
print("Category        :", category)
