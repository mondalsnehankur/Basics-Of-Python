# Q73. Vehicle Insurance Premium Calculator

age = 28
vehicle_value = 800000
accident_history = False

base_rate = 0.03
if age < 25:
    base_rate += 0.005
if accident_history:
    base_rate += 0.01

premium = vehicle_value * base_rate

print(f"Driver Age      : {age}")
print(f"Vehicle Value   : Rs. {vehicle_value}")
print(f"Accident History: {accident_history}")
print(f"Premium Rate    : {base_rate * 100:.1f}%")
print(f"Insurance Premium: Rs. {premium:.2f}")
