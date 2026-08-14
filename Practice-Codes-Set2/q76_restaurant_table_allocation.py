# Q76. Restaurant Table Allocation System

guests = 8
reservation = "VIP"

if reservation == "VIP":
    table = "VIP Lounge"
elif guests <= 2:
    table = "Small Table"
elif guests <= 5:
    table = "Medium Table"
else:
    table = "Large Table"

print(f"Guests          : {guests}")
print(f"Reservation     : {reservation}")
print(f"Allocated       : {table}")
