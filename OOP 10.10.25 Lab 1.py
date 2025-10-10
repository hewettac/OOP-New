class Book:
    def __init__(self):
        self.book_id = ""
        self.book_title = ""
        self.author_id = ""
        self.publisher = ""
        self.pub_year = ""

    def add_book(self):
        self.book_id = input("Enter Book ID: ")
        self.publisher = input("Enter Publisher: ")
        self.book_title = input("Enter Title: ")
        self.author_id = input("Enter Author ID: ")
        self.pub_year = input("Enter Year of Publication: ")

    def display_book(self):
        print("Book ID: ", self.book_id)
        print("Book Title: ", self.book_title)
        print("Author ID: ", self.author_id)
        print("Year of Publication: ", self.pub_year)
        print("Publisher: ", self.publisher)


class Author:
    def __init__(self):
        self.author_id = ""
        self.author_name = ""
        self.affiliation = ""
        self.country = ""
        self.phone = ""
        self.email_id = ""

    def add_author(self):
       self.author_id = input("Enter Author ID: ")
       self.author_name = input("Enter Author Name: ")
       self.affiliation = input("Enter Author's Affiliation: ")
       self.country = input("Enter Country: ")
       self.phone = input("Enter Author's Phone Number: ")
       self.email_id = input("Enter Author's Email: ")

    def display_author(self):
        print("Author ID: ", self.author_id)
        print("Author Name: ", self.author_name)
        print("Affiliation :", self.affiliation)
        print("Country: ", self.country)
        print("Author's Phone: ", self.phone)
        print("Author's Email: ", self.email_id)



class User:
    def __init__(self):
        self.userid = ""
        self.user_name = ""
        self.user_pass = ""
        self.user_address = ""
        self.user_phone = ""
        self.user_email_id = ""
        self.booksborrowed = []

    def add_user(self):
        self.userid = input("Enter User ID: ")
        self.user_name = input("Enter User Name: ")
        self.user_pass = input("Enter User Password: ")
        self.user_address = input("Enter User Address: ")
        self.user_phone = input("Enter User Phone Number: ")
        self.user_email_id = input("Enter User Email: ")

    def borrow_book(self, bb1):
            self.booksborrowed.append(bb1)

    def display_user(self):
        print("User ID: ", self.userid)
        print("User Name: ", self.user_name)
        print("User Password: ", self.user_pass)
        print("User Address: ", self.user_address)
        print("User Phone: ", self.user_phone)
        print("User Email: ", self.user_email_id)
        for x in self.booksborrowed:
            print("Books Borrowed: ", x.book_id, x.book_title)


## Authors

a1 = Author()
a1.add_author()

a2 = Author()
a2.add_author()

a3 = Author()
a3.add_author()

## Books

b1 = Book()
b1.add_book()

b2 = Book()
b2.add_book()

b3 = Book()
b3.add_book()

## Users

u1 = User()
u1.add_user()

u2 = User()
u2.add_user()

u3 = User()
u3.add_user()

## Add Books to users and print

u1.borrow_book(b1)
u1.borrow_book(b2)
u1.borrow_book(b3)

u2.borrow_book(b1)
u2.borrow_book(b2)
u2.borrow_book(b3)

u3.borrow_book(b1)
u3.borrow_book(b2)
u3.borrow_book(b3)

u1.display_user()
u2.display_user()
u3.display_user()