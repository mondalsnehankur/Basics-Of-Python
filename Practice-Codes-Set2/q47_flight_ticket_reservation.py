# Q47. Flight Ticket Reservation System

travel_class = "Economy"
age = 65

base_fare = 4500 if travel_class == "Economy" else 8500
fare = base_fare * 0.85 if age >= 60 else base_fare

print(f"Class           : {travel_class}")
print(f"Age             : {age}")
print(f"Fare Payable    : Rs. {fare:.2f}")
