# Q67. Banking Transaction Summary System

opening = 15000
deposit = 5000
withdrawal = 22000
final = opening + deposit - withdrawal

print(f"Opening Balance : Rs. {opening}")
print(f"Deposit         : Rs. {deposit}")
print(f"Withdrawal      : Rs. {withdrawal}")

if final < 0:
    print("Status          : Transaction Declined")
else:
    print(f"Final Balance   : Rs. {final}")
