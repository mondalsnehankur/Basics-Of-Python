# Input marks of five subjects
m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))

# Calculate total and percentage
total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

# Display results
print("Total Marks =", total)
print("Percentage =", percentage, "%")