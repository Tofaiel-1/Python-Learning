class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

# Creating an instance of the Person class
john = Person("John", 30)
# Calling the introduce method on the john instance
john.introduce()

    