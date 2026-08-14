# Q38. University Scholarship Evaluation

percentage = 85

if percentage >= 90:
    status = "Full Scholarship"
elif percentage >= 80:
    status = "50% Scholarship"
elif percentage >= 70:
    status = "25% Scholarship"
else:
    status = "No Scholarship"

print(f"Percentage      : {percentage}%")
print("Scholarship     :", status)
