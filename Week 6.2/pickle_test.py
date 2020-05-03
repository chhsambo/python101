import pickle

with open("data.pkl", "rb") as f:   # rb => read binary
    data = pickle.load(f)

print(data)