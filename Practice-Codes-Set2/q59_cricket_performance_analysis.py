# Q59. Cricket Performance Analysis System

p1 = {"Name": "Rohit", "Runs": 85, "Strike Rate": 142.5}
p2 = {"Name": "Virat", "Runs": 102, "Strike Rate": 135.0}

better = p1["Name"] if p1["Runs"] > p2["Runs"] else p2["Name"]

print(f"{p1['Name']}: {p1['Runs']} runs @ SR {p1['Strike Rate']}")
print(f"{p2['Name']}: {p2['Runs']} runs @ SR {p2['Strike Rate']}")
print("Better Performer:", better)
