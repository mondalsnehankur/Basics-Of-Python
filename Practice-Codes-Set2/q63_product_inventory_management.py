# Q63. Product Inventory Management System

product = {"Name": "USB Drive", "Unit Price": 350, "Stock": 40}
total_value = product["Unit Price"] * product["Stock"]
product["Stock"] -= 5

print(f"Product         : {product['Name']}")
print(f"Total Value     : Rs. {total_value}")
print(f"Updated Stock   : {product['Stock']} units")
