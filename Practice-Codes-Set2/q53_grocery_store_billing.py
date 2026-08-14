# Q53. Grocery Store Billing System

prices = [120, 250, 85, 310, 175]
total = sum(prices)
gst = total * 0.08
final = total + gst

print(f"Item Prices     : {prices}")
print(f"Highest Price   : Rs. {max(prices)}")
print(f"Lowest Price    : Rs. {min(prices)}")
print(f"Subtotal        : Rs. {total}")
print(f"GST (8%)        : Rs. {gst:.2f}")
print(f"Final Bill      : Rs. {final:.2f}")
