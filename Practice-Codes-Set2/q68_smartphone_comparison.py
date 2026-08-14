# Q68. Smartphone Comparison System

s1 = {"Brand": "Samsung", "Model": "Galaxy A54", "Price": 38000, "RAM": "8GB", "Storage": "128GB"}
s2 = {"Brand": "OnePlus", "Model": "Nord CE 3", "Price": 26000, "RAM": "8GB", "Storage": "128GB"}

economical = s1 if s1["Price"] < s2["Price"] else s2

print(f"{s1['Brand']} {s1['Model']}: Rs. {s1['Price']}")
print(f"{s2['Brand']} {s2['Model']}: Rs. {s2['Price']}")
print(f"More Economical : {economical['Brand']} {economical['Model']}")
