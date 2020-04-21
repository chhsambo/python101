# Data Structure
# - List
# - Dictinary
# - Tuple
# - Set

l1 = ["a", "b", "c"]
d1 = {
    "a": 1,
    "b": 2,
    "c": 3
}
t1 = ("a", "b", "c")
t1[0]   # "a"

gender = ("Male", "Female")
department = ("CS", "English", "Medical")

l1.append("a")
l1.append("d")

s1 = set(l1)
l2 = sorted(list(s1))
# print(s1)
# print(l2)

s1.add("e")
s1.add("f")


print(sorted(d1.items()))

result = [('a', 1), ('b', 2), ('c', 3)]

result1 = result[0]     # ('a', 1)
# print(result[0][0])

result.append("test")
result[3] = "Hello"
print(result)

print(result1)
result1[0] = "b"
print(result1[0])
