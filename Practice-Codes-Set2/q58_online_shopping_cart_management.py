# Q58. Online Shopping Cart Management

cart = ["Phone", "Tablet", "Watch", "Earbuds", "Charger"]
cancelled = "Watch"
pos = cart.index(cancelled)
cart.remove(cancelled)
cart.insert(pos, "SmartBand")

print("Updated Cart    :", cart)
