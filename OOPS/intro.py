user_name=(input("Enter your name"))
user_age=int(input("Enter your age"))
class person:

    def __init__(self,name,age):
        self.name=name
        self.age=age 

    def intro(self):
            return f"Hello my name is{self.name} and i am {self.age} years old"
        

p1=person(user_name,user_age)
print(p1.intro())

