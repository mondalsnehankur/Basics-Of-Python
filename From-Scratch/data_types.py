values = [
    42, 3.14, 2+3j, True, "Python", None,
    [1, 2], (1,2), {1,2}, {'name': 'Maitreyee'}
]
print("Data Types of the values in the list:")
for value in values:
    print(f"{value}: {type(value)}")
