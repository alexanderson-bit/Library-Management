class Book:
    def __init__(self,title,writer,quantity=1):
        self.quantity=quantity
        self.borrowed=0
        self.set_title(title)
        self.set_writer(writer)
        self.set_borrowed(0)
        self.set_available()

    def set_title(self,title):
        self.title=title
    def set_writer(self,writer):
        self.writer=writer
    def set_available(self):
        self.available=self.quantity-self.borrowed
    def set_borrowed(self,borrowed):
        self.borrowed+=borrowed
    def set_quantity(self,quantity):
        self.quantity+=quantity

    def get_title(self):
        return self.title
    def get_writer(self):
        return self.writer
    def get_available(self):
        self.available
    def get_borrowed(self):
        self.borrowedx
    

    def borrowingـbook():
        ...
    def returningـbook():
        ...

    def __str__(self):
        m=f"title:{self.title} writer:{self.writer} Borrowed:{}"
