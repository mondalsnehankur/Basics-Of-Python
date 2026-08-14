# Q52. Student Academic Performance Report

marks = [88, 76, 91, 65, 80]
total = sum(marks)
percentage = total / 500 * 100
highest = max(marks)
lowest = min(marks)

if percentage >= 90:
    grade = "O"
elif percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
else:
    grade = "C"

print(f"Marks           : {marks}")
print(f"Total           : {total}/500")
print(f"Percentage      : {percentage:.2f}%")
print(f"Highest Mark    : {highest}")
print(f"Lowest Mark     : {lowest}")
print(f"Grade           : {grade}")
