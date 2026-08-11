class User:
    def __init__(self,national_code,fname,lname,city,dad_name,password):
        self.id_book=0
        self.books=[]
        self.set_national_code(national_code)
        self.set_name(fname,lname)
        self.set_city(city)
        self.set_dad_name(dad_name)
        self.set_password(password) 

    def set_national_code(self,national_code):
        self.national_code=national_code
    def set_name(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def set_city(self,city):
        self.city=city
    def set_dad_name(self,dad_name):
        self.dad_name=dad_name
    def set_password(self,password):
        self.__password=password    

    def get_national_code(self):
        return self.national_code
    def get_password(self):
        return self.__password
    def get_name(self):
        return self.fname+''+self.lname
    def get_books(self):
        return self.books

    def check_borrowing_limit(self):
        return self.id_book<=4

    def add_book(self,book):
            self.id_book+=1
            self.books.append(book)
        

    def delete_book(self,book):
        books2=self.books.copy()
        for i in books2:
            if i[0]==book[0] and i[1]==book[1]:
                self.books().remove(book)
                self.id_book-=1
                return True
        return False    
