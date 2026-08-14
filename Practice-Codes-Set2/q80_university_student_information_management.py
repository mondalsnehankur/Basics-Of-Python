# Q80. University Student Information Management System

name = "Arjun Verma"
reg_no = "2024CS101"
department = "Computer Science"
marks = [88, 76, 91, 65, 82]
hostel = True
annual_income = 250000

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

print("=" * 45)
print("           STUDENT REPORT")
print("=" * 45)
print(f"Name            : {name}")
print(f"Reg. No.        : {reg_no}")
print(f"Department      : {department}")
print(f"Marks           : {marks}")
print(f"Total           : {total}/500")
print(f"Percentage      : {percentage:.2f}%")
print(f"Highest Mark    : {highest}")
print(f"Lowest Mark     : {lowest}")
print(f"Grade           : {grade}")
print("-" * 45)
if annual_income < 300000 and percentage >= 80:
    print("Eligible for Merit-cum-Means Scholarship")
if hostel:
    print("Hostel Allocation Request Generated")
print("=" * 45)
