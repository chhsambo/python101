import csv

# with open("users.csv", mode="w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["ID", "Username", "Password"])
#     writer.writerow([1, "user1", "pass1"])
#     writer.writerow([2, "user2", "pass2"])

users = [
    [1, "user1", "pass1"],
    [2, "user2", "pass2"],
    [3, "user3", "pass3"] 
]
# mode: "r", "w", "a", "w+", "a+"
with open("users.csv", mode="a", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(users)
