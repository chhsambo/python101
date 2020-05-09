# Method 1 - Simple Variable
book_title = "English Book 1"
book_number_of_page = 98

book_title2 = "English Book 2"
book_number_of_page2 = 80

# Method 2 - Use Data Structure
books = [
    {
        "title": "English Book 1",
        "number_of_page": 98
    },
    {
        "title": "English Book 2",
        "number_of_page": 80
    }
]

# Method 3 - Use Class

# Create class
class Book:

    creator = "Sambo"

    # object's attribute
    def __init__(self, book_title="", book_author="", number_of_page=0):  # init => initialize
        self.title = book_title
        self.author = book_author
        self.number_of_page = number_of_page

    # Instance methods (object's method)
    def details(self):
        return f"Book {self.title} written by {self.author} has {self.number_of_page} pages."

    def borrow(self, borrower):
        print(self.details())
        print(f"{self.title} borrowed by {borrower}")
    
# Create Instance object of Class Book
book = Book()
book1 = Book("Book 1", "Uncle Bob", 98)
book2 = Book("Book 2")
book3 = Book("Book 3")

book1.creator = "Unknown"
book1.borrow("Sau")


# print(book1)
# print(book2)
# print(book3)

# book4 = book1
# print(book4)
# if book4 == book1:
#     print("Book 4 is the same as Book 1")

# if book2 == book1:
#     print("Book 2 is the same as Book 1")

# book1.creator = "Unknown"
# Book.creator = "Unknown"
# print(book1.creator)
# print(book2.creator)

# print(f"Book {book1.title} written by {book1.author} has {book1.number_of_page} pages.")
# print(book1.details())
# print(book2.details())
# print(book3.details())

# book1.borrow("Sok")