import pickle
class name:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,"  ",self.age)

m1=name("komeil mahdavi",21)
pickle.dump(m1, open('data.pkl', 'wb'))
m2=name("ali mahdvvi",21)
pickle.dump(m2, open('data.pkl', 'ab'))
with open('data.pkl', 'rb') as f:
    for i in range (3):
        loaded = pickle.load(f)
        loaded.show()
