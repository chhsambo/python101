def get_fruits_list():
    fruits_file = open("fruits.txt")
    fruits = fruits_file.read()

    fruits = fruits.replace(", ", ",").lower()
    fruits = fruits.split("\n")
    fruits = ",".join(fruits)
    fruits = fruits.split(",")
    # print(fruits)
    return fruits
    