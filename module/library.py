from .book import Book
from .user import User

class Library:
    def __init__(self):
        self.users=[]
        self.books=[]

    def get_books(self):
        return self.books
    def get_user(self):
        return self.users
    

    def create_book(self,title,writer):
        book=self.check_book(title,writer)
        if book:
            book.set_update_quantity()
            return False
        else:
            self.books.append(Book(title,writer))
            return True
    
    def check_book(self,title,writer):
        for book in self.books:
            if book.get_title()==title and book.get_writer()==writer:
                return book
        return False    

    def create_user(self,national_code,fname,lname,city,dad_name,password):
        if self.check_duplicate(national_code):
            return False
        else:
            user=User(national_code,fname,lname,city,dad_name,password)
            self.users.append(user)
            return user

    def check_duplicate(self,national_code):
        for user in self.users: 
            if user.get_national_code()==national_code:
                return True
        return False    

    
    def check_login_user(self,national_code,password):
        for user in self.users:
            if user.get_national_code==national_code and user.get_password()==password:
                return user
        return False    

    def returningـbook(self,title,writer):
        book=self.check_book(title,writer)
        if book:
            if book.check_returning():
                return False
            else:
                book.returningـbook()
                return True
        else:
            return False 

    def borrowingـbook(self,title,writer):
        book=self.check_book(title,writer)
        if book and book.borrowingـbook():
            return book
        else:
            return False

    def borrowing(self,user,title,writer):
        if user.check_borrowing_limit():
            book=self.borrowingـbook(title,writer)
            if book:
                user.add_book(book)
                return "The book was successfully borrowed."
            else:
                return "The book is on loan."
        else:
            return "Books borrowed exceeding the allowed limit"

def returningـbook(self,user,title):
    pass