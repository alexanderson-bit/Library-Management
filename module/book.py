class Book:
    def __init__(self,title,writer):
        self.quantity=1
        self.borrowed=0
        self.available=1
        self.set_title(title)
        self.set_writer(writer)

    def set_title(self,title):
        self.title=title
    def set_writer(self,writer):
        self.writer=writer

    def set_update_quantity(self):
        self.quantity+=1

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
    def check_returning(self):
        if self.available==self.quantity:
            return False
        return True
    def borrowingـbook(self):
        if self.check_status():
            self.borrowed+=1
            self.available=self.get_quantity()-self.get_borrowed()
            return True
        else:
            return False

    def returningـbook(self):
        self.borrowed-=1
        self.available=self.get_quantity()-self.get_borrowed()

    def __str__(self):
        return f"title:{self.title} writer:{self.writer} quantity:{self.quantity} available:{self.available}"
