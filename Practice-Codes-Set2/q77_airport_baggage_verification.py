# Q77. Airport Baggage Verification System

baggage_weight = 22

if baggage_weight <= 20:
    status = "No Extra Charge"
elif baggage_weight <= 30:
    status = "Excess Baggage Charge: Rs. 500"
else:
    status = "Not Allowed"

print(f"Baggage Weight  : {baggage_weight} kg")
print("Status          :", status)
