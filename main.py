import string
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



m=checking_strong_password()
print(m)