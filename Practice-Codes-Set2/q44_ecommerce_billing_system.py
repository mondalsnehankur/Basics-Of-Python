# Q44. E-Commerce Billing System

p1, q1 = 800, 2
p2, q2 = 1500, 1
p3, q3 = 600, 3

subtotal = p1 * q1 + p2 * q2 + p3 * q3
discount = subtotal * 0.10 if subtotal > 5000 else 0
after_discount = subtotal - discount
gst = after_discount * 0.18
total = after_discount + gst

print(f"Subtotal        : Rs. {subtotal}")
print(f"Discount (10%)  : Rs. {discount}")
print(f"GST (18%)       : Rs. {gst:.2f}")
print(f"Final Amount    : Rs. {total:.2f}")
