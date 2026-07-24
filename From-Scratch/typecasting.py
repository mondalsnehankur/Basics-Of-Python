age_text = "20"
age_number = int(age_text)
price = float("149.75")
count_text = str(15)

print(age_number + 5)
print(price, type(price))
print(count_text,type(count_text))

# Collections can also be converted
numbers = [1,2,2,3,4]
print(tuple(numbers))
print(set(numbers)) # Duplicate values will be removed