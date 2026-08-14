# Q55. Employee Record Management System

emp = {"Name": "Kavitha", "Department": "HR", "Designation": "Executive", "Salary": 40000}
emp["Department"] = "Management"
emp["Salary"] = 55000

print("Updated Employee Record:")
for k, v in emp.items():
    print(f"  {k}: {v}")
