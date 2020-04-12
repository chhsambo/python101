def find_index(custom_list, value):
    i = 0
    for x in custom_list:
        if x == value:
            return i
        i+=1
    return None


simple_list = [1, 2, 3]

another_list = ["apple", "grape", "banana"]

mix_list = [1, 2, 3, "apple", "grape", "banana"]

alldata = ["Phnom Penh", 123, [1, 2]]

# index_grape = find_index(mix_list, "grape")
# print(f"grape at index {index_grape}")

index_pp = find_index(alldata, "Phnom ")
print(index_pp)


# print(mix_list[3])

# print(alldata[0].upper())
# print(alldata[1] + 2)
# print(alldata[2][0])

# # Using `for` on list
# for x in alldata:
#     if type(x) is list:
#         print(f"{x} : {type(x)}")