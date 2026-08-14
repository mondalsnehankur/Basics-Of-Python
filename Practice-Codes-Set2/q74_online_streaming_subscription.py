# Q74. Online Streaming Subscription System

plan = "Standard"

if plan == "Basic":
    charge = 149
    features = "SD Quality, 1 Screen"
elif plan == "Standard":
    charge = 299
    features = "HD Quality, 2 Screens"
elif plan == "Premium":
    charge = 549
    features = "4K Quality, 4 Screens, Downloads"
else:
    charge = 0
    features = "Invalid Plan"

print(f"Plan            : {plan}")
print(f"Monthly Charge  : Rs. {charge}")
print(f"Features        : {features}")
