# Q39. E-Commerce Delivery Charge Calculator

order_value = 1500

if order_value > 2000:
    msg = "Free Delivery"
elif order_value >= 1000:
    msg = "Delivery Charge: Rs. 50"
else:
    msg = "Delivery Charge: Rs. 100"

print(f"Order Value     : Rs. {order_value}")
print("Delivery        :", msg)
