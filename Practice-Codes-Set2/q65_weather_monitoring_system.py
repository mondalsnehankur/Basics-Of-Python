# Q65. Weather Monitoring System

celsius = 22
fahrenheit = (celsius * 9/5) + 32

if celsius < 15:
    category = "Cold"
elif celsius <= 30:
    category = "Pleasant"
else:
    category = "Hot"

print(f"Temperature     : {celsius} C")
print(f"In Fahrenheit   : {fahrenheit} F")
print("Weather         :", category)
