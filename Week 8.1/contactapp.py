# Convention: PEP8
class Contact:
    
    def __init__(self, name, tel, position=None, org=None, email=None, fb=None):
        self.name = name
        self.position = position
        self.organization = org
        self.telephone = tel
        self.email = email
        self.facebook = fb
        self.__photo = None

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


class FamilyContact(Contact):

    # Overwrite __init__() in superclass (Contact)
    def __init__(self, name, tel, position=None, org=None, email=None, fb=None, relationship=None):
        super().__init__(name, tel, position, org, email, fb)
        # Contact.__init__(self, name, tel, position, org, email, fb)
        self.relationship = relationship

    def get_relationship(self):
        return self.relationship

    def is_sibling(self):
        sibling = ["sister", "brother"]
        # if self.relationship.lower() == "sister" or self.relationship.lower() == "brother":
        if self.relationship.lower() in sibling:
            return True

        return False

    def print(self):
        super().print()
        if self.relationship:
            print("- Relationship: " + self.relationship)


f1 = FamilyContact(
    name="Sopheak",
    tel="016 675666",
    relationship="Brother"
)
f1.print()
if f1.is_sibling():
    print(f"{f1.name} is my sibling")

sok = Contact(
    name="Sok",
    tel="012334455"
)
# if sok.is_sibling(): # Error
#     pass


def load_contacts():
    sok = Contact("Sok", "012 343434", email="sok@gmail.com", position="Sale", org="ICE")
    sau = Contact("Sau", "011 456654", position="Technical", org="ICE")
    minea = Contact("Minea", "010 233244", position="Project Manager", org="ICE")
    tola = Contact("Tola", "012 556677", fb="fb.com/tola.kh")

    return [sok, sau, minea, tola]


mycontact_list = load_contacts()


# Return contact or None
def search_contact(search_name):
    for contact in mycontact_list:
        if contact.name.lower() == search_name:
            return contact
    else:
        return None


def new_contact(contact):
    mycontact_list.append(contact)


print("""
Choose action you want to do:
1) List all contact
2) Search contact
3) New contact
""")
selection = input("Enter number: ")

if selection == "1":
    Contact.print_all(mycontact_list)

elif selection == "2":
    name_input = input("Enter name (or \q to quit): ")
    name_input = name_input.lower()

    result = search_contact(name_input)
    if result:
        result.print()
    else:
        print("No contact found!")

elif selection == "3":
    name = input("Name: ")
    tel = input("Telephone: ")
    position = input("Position: ")
    org = input("Organization: ")
    email = input("Email: ")
    fb = input("Facebook: ")
    
    contact = Contact(
        name=name,
        tel=tel,
        position=position,
        org=org,
        email=email,
        fb=fb
    )
    new_contact(contact)

else:
    print("Invalid selection")


# .pop() : to delete item from list