import random
firstname_list=[
    "Emma", "Olivia", "Ava", "Isabella", "Sophia"
    ,"Charlotte", "Mia", "Amelia", "Harper", "Evelyn"
]
lastname_list=[
    "Abigail", "Emily", "Elizabeth", "Mila", "Ella"
    , "Avery", "Sofia", "Camila", "Aria", "Scarlett"
]
firstname=random.randint(0,9)
lastname=random.randint(0,9)
print(f"Fullname : {firstname_list[firstname]} {lastname_list[lastname]}")
#print("Fullname : %s %s"%(firstname_list[firstname],lastname_list[lastname]))
#print("Fullname : {0} {1}".format(firstname_list[firstname],lastname_list[lastname]))