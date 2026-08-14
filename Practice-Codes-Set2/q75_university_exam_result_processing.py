# Q75. University Examination Result Processing System

marks = [55, 40, 72, 38, 61]
total = sum(marks)
percentage = total / 500 * 100
passed_all = all(m >= 35 for m in marks)
result = "Pass" if passed_all and percentage >= 40 else "Fail"

print(f"Marks           : {marks}")
print(f"Total           : {total}/500")
print(f"Percentage      : {percentage:.2f}%")
print(f"Result          : {result}")
