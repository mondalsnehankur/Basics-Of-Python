# Q50. Banking Interest Calculator

principal = 600000
rate = 7.0
time = 3

if principal > 500000:
    rate += 0.5

interest = (principal * rate * time) / 100
total = principal + interest

print(f"Principal       : Rs. {principal}")
print(f"Rate of Interest: {rate}%")
print(f"Simple Interest : Rs. {interest}")
print(f"Total Amount    : Rs. {total}")
