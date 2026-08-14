# Q41. University Admission Eligibility System

scores = [88, 76, 90]
avg = sum(scores) / len(scores)

if avg >= 85:
    status = "Direct Admission"
elif avg >= 70:
    status = "Interview Round"
else:
    status = "Not Eligible"

print(f"Scores          : {scores}")
print(f"Average         : {avg:.2f}")
print("Admission Status:", status)
