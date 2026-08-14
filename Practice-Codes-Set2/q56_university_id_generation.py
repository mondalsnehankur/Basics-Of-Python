# Q56. University ID Generation System

first = "Aarav"
last = "Mehta"
reg_no = "REG2024"
year = "2024"

uid = f"{year}-{first[:3].upper()}-{last[:3].upper()}-{reg_no}"
print("University ID   :", uid)
