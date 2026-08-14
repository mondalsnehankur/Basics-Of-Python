# Q43. Employee Performance Evaluation System

attendance = 90
project_score = 78
client_feedback = 8

weighted = (attendance * 0.20) + (project_score * 0.50) + (client_feedback * 10 * 0.30)

if weighted >= 85:
    category = "Excellent"
elif weighted >= 70:
    category = "Good"
elif weighted >= 50:
    category = "Average"
else:
    category = "Poor"

print(f"Weighted Score  : {weighted:.2f}")
print("Performance     :", category)
