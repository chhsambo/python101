# Convention: PEP8
class Contact:
    
    def __init__(self, name, tel, position=None, org=None, email=None, fb=None):
        self.name = name
        self.position = position
        self.organization = org
        self.telephone = tel
        self.email = email
        self.facebook = fb

    @staticmethod
    def print_all(mycontact_list):
        print("All Contacts")
        for contact in mycontact_list:
            print(contact.name + " : " + contact.telephone)

    def print(self):
        print(self.name)
        print("- Telephone: " + self.telephone)
        if self.position:
            print("- Position: " + self.position)
        if self.organization:
            print("- Organization: " + self.organization)
        if self.email:
            print("- Email: " + self.email)
        if self.facebook:
            print("- Facebook: " + self.facebook)


def load_contacts():
    sok = Contact("Sok", "012 343434", position="Sale", org="ICE")
    sau = Contact("Sau", "011 456654", position="Technical", org="ICE")
    minea = Contact("Minea", "010 233244", position="Project Manager", org="ICE")
    tola = Contact("Tola", "012 556677", fb="fb.com/tola.kh")
    # sok.print()
    # sau.print()
    
    return [sok, sau, minea, tola]


mycontact_list = load_contacts()
Contact.print_all(mycontact_list)

name_input = input("Enter name you want to see detail (or \q to quit): ")
name_input = name_input.lower()

for contact in mycontact_list:
    if contact.name.lower() == name_input:
        contact.print()
        break
else:
    print("No contact found!")

# Task: Create method for search contact by name