# Q51. Hospital Patient Billing System

patient = {"Name": "Ramya", "Room": 101, "Consultation": 500, "Room Charges": 2000}
patient["Room"] = 205
total_bill = patient["Consultation"] + patient["Room Charges"]

print("Patient Name    :", patient["Name"])
print("Room Number     :", patient["Room"])
print("Consultation    : Rs.", patient["Consultation"])
print("Room Charges    : Rs.", patient["Room Charges"])
print("Total Bill      : Rs.", total_bill)
