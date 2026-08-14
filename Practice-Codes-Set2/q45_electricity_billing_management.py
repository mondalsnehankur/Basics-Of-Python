# Q45. Electricity Billing Management System

units = 450

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (200 * 7) + (units - 300) * 10

total = bill + 150

print(f"Units           : {units}")
print(f"Bill Amount     : Rs. {bill}")
print(f"Maintenance     : Rs. 150")
print(f"Total Bill      : Rs. {total}")
