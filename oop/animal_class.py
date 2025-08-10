class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        return f"{self.name} eats."

    def sleep(self):
        return f"{self.name} sleeps."


class Dog(Animal):
    def __init__(self, name, age, breed):
        # Call the parent constructor
        super().__init__(name, age)
        self.breed = breed
    def bark(self):
        return f"{self.name} says woof wooof!."


    def info(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}."

dog1 = Dog('Buddy', 12, 'German Shephered')

print(dog1.info())    # Buddy is a 12-year-old German Shephered.
print(dog1.bark())    # Buddy says woof wooof!.
print(dog1.sleep())   # Buddy sleeps. (inherited from Animal)