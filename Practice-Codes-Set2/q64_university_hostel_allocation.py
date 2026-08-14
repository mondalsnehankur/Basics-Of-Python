# Q64. University Hostel Allocation System

annual_income = 180000

if annual_income <= 200000:
    hostel = "AC Hostel"
elif annual_income <= 500000:
    hostel = "Non-AC Hostel"
else:
    hostel = "Waiting List"

print(f"Annual Income   : Rs. {annual_income}")
print("Hostel Allocated:", hostel)
