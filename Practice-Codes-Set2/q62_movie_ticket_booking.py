# Q62. Movie Ticket Booking System

ticket_price = 250
num_tickets = 4
convenience_fee = 30
gst_percent = 18

subtotal = ticket_price * num_tickets
gst = (subtotal + convenience_fee) * gst_percent / 100
total = subtotal + convenience_fee + gst

print(f"Ticket Price    : Rs. {ticket_price}")
print(f"No. of Tickets  : {num_tickets}")
print(f"Convenience Fee : Rs. {convenience_fee}")
print(f"GST (18%)       : Rs. {gst:.2f}")
print(f"Total Payable   : Rs. {total:.2f}")
