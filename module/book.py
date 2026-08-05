class Book:
    def __init__(self,title,writer,quantity=1):
        self.quantity=quantity
        self.borrowed=0
        self.available=quantity
        self.set_title(title)
        self.set_writer(writer)

    def set_title(self,title):
        self.title=title
    def set_writer(self,writer):
        self.writer=writer

    def set_quantity(self,quantity):
        self.quantity+=quantity

    def get_title(self):
        return self.title
    def get_writer(self):
        return self.writer
    def get_available(self):
        return self.available
    def get_borrowed(self):
        return self.borrowed
    def get_quantity(self):
        return self.quantity

    def check_status(self):
        if self.borrowed<self.quantity:
            return True
        else:
            return False

    def borrowingـbook(self):
        if self.check_status(self):
            self.borrowed+=1
            self.available=self.get_quantity()-self.get_borrowed()
            return False
        else:
            return True

    def returningـbook(self):
        self.borrowed+=1
        self.available=self.get_quantity()-self.get_borrowed()

    def __str__(self):
        m=f"title:{self.get_title()} writer:{self.get_writer()} quantity:{self.get_quantity()} available:{self.get_available}"
