# Q46. Online Food Ordering System

food_bill = 1600
delivery = 0 if food_bill > 800 else 50
discount = food_bill * 0.05 if food_bill > 1500 else 0
after_discount = food_bill - discount
gst = after_discount * 0.05
total = after_discount + gst + delivery

print(f"Food Bill       : Rs. {food_bill}")
print(f"Discount (5%)   : Rs. {discount}")
print(f"GST (5%)        : Rs. {gst:.2f}")
print(f"Delivery Charge : Rs. {delivery}")
print(f"Final Amount    : Rs. {total:.2f}")
