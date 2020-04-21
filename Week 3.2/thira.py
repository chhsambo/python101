Sokunthira = {
    'Name' : 'Ly Sokunthira',
    'Sex' : 'Male',
    'Phone' : '077303533',
    'Email' : 'serverthira0826@gmail.com',
}
khemrin = {
    'Name' : 'Ly khemrin',
    'Sex' : 'Male',
    'Phone' : '123456789',
    'Email' : 'serverthira2630@gmail.com',
}
chheanglim = {
    'Name' : 'chheanglim',
    'Sex' : 'Female',
    'Phone' : '123456789',
    'Email' : 'chheanglim@gmail.com',
}
thearak = {
    'Name' : 'thearak',
    'Sex' : 'male',
    'Phone' : '123456789',
    'Email' : 'thearak@gmail.com',
}
i = 0
mycontacts = [Sokunthira,khemrin,chheanglim,thearak]
usname = input("Type Contact Name : ").lower()  

for contact in mycontacts:
    if usname == contact['Name'].lower():
        for found in contact.items():
            print(f"- {found[0]} : {found[1]}")
            i = 1
if i != 1: 
    print("Username not found")