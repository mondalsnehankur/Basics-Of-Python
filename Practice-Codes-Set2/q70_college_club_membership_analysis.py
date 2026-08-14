# Q70. College Club Membership Analysis

coding = {"Alice", "Bob", "Charlie", "Diana", "Eve"}
ai_club = {"Bob", "Diana", "Frank", "Grace", "Alice"}

both = coding & ai_club
either = coding | ai_club
only_coding = coding - ai_club

print("Both Clubs       :", sorted(both))
print("Either Club      :", sorted(either))
print("Only Coding Club :", sorted(only_coding))
