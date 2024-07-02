class Person:

    def __init__(self, name=None, age=None, address=None):
        if name is None:
            name = input("Enter name: ")
        if age is None:
            age = int(input("Enter age: "))
        if address is None:
            address = input("Enter address: ")
            
        self.name = name
        self.age = age
        self.address = address

    def introduce(self):
        print(f'I am {self.name} from {self.address} and {self.age} years old.')





















# @classmethod
#     def create(cls):
#         name = input("Enter name: ")
#         age = int(input("Enter age: "))
#         address = input("Enter address: ")
#         return cls(name, age, address)











# class Person:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address


#     def introduce(self):
#         print(f'I am {self.name} from {self.address} and {self.age} years old.')