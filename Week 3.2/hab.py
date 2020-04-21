#Search name in dictionary

kimarvata = {
    'name'  :   'kimarvata',
    'sex'   :   'm',
    'phone' :   '010101010',
    'email' :   'kimarvata@gmail.com',
}
soksokha = {
    'name'  :   'soksokha',
    'sex'   :   'f',
    'phone' :   '012121212',
    'email' :   'soksokha@gmail.com',
}
sounchai = {
    'name'  :   'sounchai',
    'sex'   :   'm',
    'phone' :   '011111111',
    'email' :   'sounchai@gmail.com',
}
soksreynae = {
    'name'  :   'soksreynae',
    'sex'   :   'f',
    'phone' :   '016121212',
    'email' :   'soksreynae@gmail.com',
}
sanbuntha = {
    'name'  :   'sanbuntha',
    'sex'   :   'm',
    'phone' :   '013111111',
    'email' :   'sounchai@gmail.com',
}
chansreynouch = {
    'name'  :   'chansreynouch',
    'sex'   :   'f',
    'phone' :   '019909090',
    'email' :   'chansreynouch@gmail.com',
}

mycontact = [kimarvata,soksokha,sounchai,soksreynae,sanbuntha,chansreynouch]
usname = input("Type UserName : ").lower()  

i = 0
for item in mycontact:
    if usname == item['name']:
        for item1 in item.items():
            print(f"- {item1[0]} : {item1[1]}")
            i = 1
if i != 1: 
    print("Username not found")


