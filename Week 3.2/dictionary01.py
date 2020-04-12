# Dictionary

list1 = [
    'apple', 
    'banana', 
    'pineapple'
]
list2 = [10, 5, 20]

inventory = {
    'apple': 10,
    'banana': 5,
    'pineapple': 20,
    'coconut': 7,
}
# print(inventory['coconut'])
# print(inventory.get('grape'))
# print(inventory.get('grade', 0))

inventory['blueberry'] = 3
inventory['apple'] = 20
inventory.pop('banana')
del inventory['coconut']

for item in inventory.items():
    print(item)

# for item in inventory.keys():
#     print(item)

# for item in inventory.values():
#     print(item)