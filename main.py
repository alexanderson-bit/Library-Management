import string
from module import Library
# import pickle
# class name:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show(self):
#         print(self.name,"  ",self.age)

# m1=name("komeil mahdavi",21)
# pickle.dump(m1, open('data.pkl', 'wb'))
# m2=name("ali mahdvvi",21)
# pickle.dump(m2, open('data.pkl', 'ab'))
# with open('data.pkl', 'rb') as f:
#     for i in range (3):
#         loaded = pickle.load(f)
#         loaded.show()
# def _safe_password():
#     pass
library=Library()
def read_national_code():
    while True:
        national_code=input("Enter National ID (10 digits) :")
        if len(national_code)!=10:
            print("The number of digits must be ten.")
            continue
        for i in national_code:
            if "0"<=i<="9":
                pass
            else:
                print("Only numbers should be entered.")
                break

        return national_code    

def checking_strong_password():
    while True:
        sum=0
        password=input("Enter password :")
        if len(password)<8:
            print("The password must be longer than 8 characters.")
            continue
        for c in password:
            if c==" ":
                continue
        if any(c.isupper() for c in password):
            sum+=1
        if any(c.islower() for c in password):
            sum+=1
        if any(c.isdigit() for c in password):
            sum+=1
        if  any( c in string.punctuation for c in password):
            sum+=1   
        if sum==4:
            return password
        else:
            print("Password must contain at least an uppercase letter, lowercase letter, special character and at least one digit")    

def menu_main():
    menu="1-Library Registration\n\
2-Book Donation\n\
3-Log in to your account\n\
4-Book search\n\
5-create new account\n\
6-Exit"
    return menu

def menu_user():
    menu="1-Display received books\n\
2-Getting a book\n\
3-Returning a book\n\
4-Change User Password\n\
5-Book Donation\n\
6-Exit"
    return menu

def check_select(menu,min,max):
    while True:
        print(menu)
        try :
            number= int(input (f"Enter a value in the range of {min} to {max} :"))
            if min<=number<=max:
                return number
        except ValueError:
            print("It is outside the numerical range !!")            


def string_input(prompt):
    while True:
        name=input(prompt).capitalize().strip()
        if name==" ":
            print("Enter again!,Cannot be left blank.")
            continue
        return name

def show_booklist():
    book_list=library.get_books()
    if len(book_list)==0:
        print("Book list is empty")
    else:
        for index, book in  enumerate(book_list,start=1):
            print(f"{index}-{book}")

def create_read_information():
    national_code=read_national_code()
    fname=string_input("Enter the first name :")
    lname=string_input("Enter the last name:")
    city=string_input("Enter the city name:")
    dad_name=string_input("Enter your father's first name:")
    password=checking_strong_password()
    user=library.create_user(national_code,fname,lname,city,dad_name,password)
    if user:
        return user
    else:
        return False

def login_account():
    national_code=read_national_code()
    password=input("Enter password :")
    return library.check_login_user(national_code,password)

#اینجا قراره که ترو بود یعنی کتاب جدید ثبت شده یا ایکی به کتاب ها اضافه شده
def create_boook():
    title,writer=read_book()
    if library.create_book(title,writer):
        print("New book registered.")
    else :
        print("This book was already available \none more copy has been added.")

def read_book():
    title=string_input("Enter the book title :")
    writer=string_input("Enter the book's author :")    
    return title,writer

def userـPanel(user):
    print("Welcome to your account.")
    while True:
        selection=check_select(menu_user(),1,6)

        if selection==1:
            display_book(user)
        elif selection==2:
            borrowing_book(user)
        elif selection==3:
            pass
        elif selection==4:
            change_password(user)
        elif selection==5:
            create_boook()
        else:
            break

def display_book(user):
    book_list=user.get_books()
    if len(book_list)==0:
        print("Book list is empty")
    else:
        for index, book in  enumerate(book_list,start=1):
            print(f"{index}-{book}")

def borrowing_book(user):
    title,writer=read_book()
    print(library.borrowing(user,title,writer) )   

def returningـbook(user):
    pass

def change_password(user):
    new_password=checking_strong_password()
    user.set_password(new_password)
    print("Password successfully changed.")

def main():
    while True:
        selection=check_select(menu_main(),1,6)
        if selection==1:
            show_booklist()
        elif selection==2:
            create_boook()
        elif selection==3:
            user=login_account()
            if user:
                print("Login successful.")
                userـPanel(user)
            else:
                print("Incorrect password or username entered.")
        elif selection==4:
            pass
        elif selection==5:
            user=create_read_information()
            if user:
                print("User account successfully created.")
                userـPanel(user)
            else:
                print("This user account already exists.")
        else :
            break
main()
m=library.get_user()
print(len(m))