from loguru import logger 
# class User:
#     def __init__(self,ip,phone_detail,location = None):
#         self.ip = ip
#         self.phone_detail = phone_detail
#         self.location = location

#     def signup(self):
#         pass

#     def login(self):
#         pass

#     def profile_update(self):
#         pass

# user1 = User("10.123.1.10","Samsumg/Android","Delhi")
# logger.info(f"{user1}")
# logger.info(f"{user1.__dict__}")
# logger.info(f"{dir(user1)}")

# class Dog:
#     sound ="bark"

# dog1 = Dog()
# logger.info(dog1.sound)

# logger.info(Dog.sound)

class Dog:
    species ="Canine" ## This is class variable

    def __init__(self,name,age):
        self.name = name
        self.age = age

## Creating instance/objects of class 
dog1 = Dog("Buddy",3)
dog2 = Dog("Charlie",5)

logger.info(dog1.species)
logger.info(dog1.name)
logger.info(dog2.name)

## Changing the Object variable
dog1.name ="Max"
logger.info(dog1.name)

## Changing the Class variable
Dog.species = "Feline"
print(dog1.species)
print(dog2.species)

## Polymorphism
## ABility of same function in python to behave differently as per conext or situation
## Compile time Polymorphism -Method Overloading

class Calculator:
    def multiply(self, a=1,b=1,*args):
        result = a*b
        for num in args:
            result *= num
        return result
calc = Calculator()

print(calc.multiply())
print(calc.multiply(4))

print(calc.multiply(2,3))
print(calc.multiply(2,3,4))

## Runtime Polymorphism - Method Overriding

class Animal:
    def sound(self):
        return "Generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        return "Meow"
    
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())

## Inheritance in Python
## super() function is used to call the parent class Constructor
class Animal:
    def __init__(self,name):
        self.name = name
    def info(self):
        print("Animal Name:",self.name)

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

    def details(self):
        print(self.name,"is a",self.breed)


d = Dog("Buddy")
d.info()
d.details()
## Python does support multiple inheritance but it is not recommended as good practice



