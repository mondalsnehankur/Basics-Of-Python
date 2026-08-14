# Q48. Mobile Recharge Recommendation System

amount = 599

if 199 <= amount <= 399:
    plan = "1 GB/day"
elif 400 <= amount <= 699:
    plan = "2 GB/day"
elif amount >= 700:
    plan = "3 GB/day + OTT Subscription"
else:
    plan = "No Plan Available"

print(f"Recharge Amount : Rs. {amount}")
print("Recommended Plan:", plan)
