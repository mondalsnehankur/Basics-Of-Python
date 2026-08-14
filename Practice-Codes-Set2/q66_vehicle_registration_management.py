# Q66. Vehicle Registration Management System

vehicle = {
    "Reg No": "MH12AB1234",
    "Owner": "Suresh Patel",
    "Address": "Pune",
    "Model": "Honda City"
}
vehicle["Address"] = "Mumbai"

print("Updated Vehicle Record:")
for k, v in vehicle.items():
    print(f"  {k}: {v}")
