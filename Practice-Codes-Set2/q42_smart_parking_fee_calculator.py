# Q42. Smart Parking Fee Calculator

hours = 7

if hours <= 2:
    fee = hours * 30
elif hours <= 5:
    fee = (2 * 30) + (hours - 2) * 20
else:
    fee = (2 * 30) + (3 * 20) + (hours - 5) * 15

print(f"Parking Hours   : {hours}")
print(f"Total Fee       : Rs. {fee}")
