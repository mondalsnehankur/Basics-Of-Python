# Q60. University Attendance Monitoring System

attendance = 72

if attendance >= 75:
    status = "Eligible for Examination"
elif attendance >= 65:
    status = "Conditionally Eligible"
else:
    status = "Not Eligible"

print(f"Attendance      : {attendance}%")
print("Status          :", status)
