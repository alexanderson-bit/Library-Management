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
        for i in national_code:
            if "0"<=i<="9":
                pass
            else:
                print("Only numbers should be entered.")
                break
        else:
            if len(national_code)==10:
                return national_code    
            else:
                print("The number of digits must be ten.")


m=read_national_code()
print(m)            