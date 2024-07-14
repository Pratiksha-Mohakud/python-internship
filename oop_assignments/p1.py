
# creating a class person with name,age and gender as attributes
class person():
    def __init__(self,name,age,gender): # initializing the attributes
        self.name=name
        self.age=age
        self.gender=gender
    def introduce(self): # defining a method to introduce the person
        return f"The person's name is {self.name} age is {self.age} and gender is {self.gender}"

# taking inputs from user
name=input("Enter name: ")
age=int(input("Enter age: "))
gender=input("Enter gender: ")

obj=person(name,age,gender)  # passing the inputs to class
print(obj.introduce())  # printing the introduction using method defined under class
