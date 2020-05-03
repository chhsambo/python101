import json


# Read data.json
with open("data.json") as f:
    data = json.load(f)

products = data["products"]

p3 = {
    "id": 103,
    "name": "product3"
}
data["products"].append(p3)

for p in data["products"]:
    print(p)

# Write data to data.json
with open("data.json", "w") as f:
    json.dump(data, f)


# Pickle
import pickle

# Write data to data.pkl
with open("data.pkl", "wb") as f:   # wb => write binary
    pickle.dump(data, f)