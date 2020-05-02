# Working with CSV Data
# Read CSV
import csv

products = []
with open("Products list - Sheet1.csv") as f:
    data = csv.reader(f)
    for row in data:
        products.append(row)

products = products[1:]
# print(products)

search = input("Enter product name: ")
result = []
for product in products:
    if product[1] == search:
        result = product

print(result)