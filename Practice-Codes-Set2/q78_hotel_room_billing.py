# Q78. Hotel Room Billing System

room_type = "Deluxe"
days = 3
base_rate = 4500
discount_pct = 10
gst_pct = 12

subtotal = base_rate * days
discount = subtotal * discount_pct / 100
after_discount = subtotal - discount
gst = after_discount * gst_pct / 100
total = after_discount + gst

print(f"Room Type       : {room_type}")
print(f"Days Stayed     : {days}")
print(f"Subtotal        : Rs. {subtotal}")
print(f"Discount ({discount_pct}%)  : Rs. {discount}")
print(f"GST ({gst_pct}%)      : Rs. {gst:.2f}")
print(f"Total Bill      : Rs. {total:.2f}")
