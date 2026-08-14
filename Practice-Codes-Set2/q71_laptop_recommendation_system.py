# Q71. Laptop Recommendation System

budget = 55000

if budget < 35000:
    category = "Basic"
elif budget <= 65000:
    category = "Mid-Range"
else:
    category = "Premium"

print(f"Budget          : Rs. {budget}")
print("Recommended     :", category)
