# Q79. Smart Water Consumption Monitoring System

consumption = 25000

if consumption <= 10000:
    category = "Low Consumption"
    bill = consumption * 0.005
elif consumption <= 30000:
    category = "Normal Consumption"
    bill = (10000 * 0.005) + (consumption - 10000) * 0.008
else:
    category = "High Consumption"
    bill = (10000 * 0.005) + (20000 * 0.008) + (consumption - 30000) * 0.012

print(f"Consumption     : {consumption} litres")
print(f"Category        : {category}")
print(f"Water Bill      : Rs. {bill:.2f}")
