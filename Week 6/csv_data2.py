import csv

# with open("Products list - Sheet1.csv") as f:
#     data = csv.reader(f)
#     for row in data:
#         print(row)

products_list = []
with open("Products list - Sheet1.csv", encoding="utf-8") as f:
    data = csv.DictReader(f)
    for row in data:
        products_list.append(dict(row))

# print(products_list)

alienware = products_list[1]
alienware_price = products_list[1]["Price"]
print(alienware_price)