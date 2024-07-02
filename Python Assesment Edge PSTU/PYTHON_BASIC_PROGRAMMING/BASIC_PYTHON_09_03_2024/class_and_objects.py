class Person:

    def __init__(self, name , age):
        self.name = name
        self.age = age

    def introduce(self):

        print(f'The name of a Student is {self.name} and he is {self.age} years old.')

student = Person('Tota' , 22.5)

student.introduce()





        