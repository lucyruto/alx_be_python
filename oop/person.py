class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f"Farewell, {self.name}")


p = Person("Lucy", 28)
del p   # Output: Farewell, Lucy