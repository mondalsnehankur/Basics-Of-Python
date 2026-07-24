# Input the principal amount
principal = float(input("Enter principal amount: "))

# Input the rate of interest
rate = float(input("Enter rate of interest: "))

# Input the time in years
time = float(input("Enter time (in years): "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Display the result
print("Simple Interest =", simple_interest)