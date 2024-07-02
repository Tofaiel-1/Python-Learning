'''

class Student:
  def __init__(s, f, l):

      s.p = f
      s.q = l
  def printname(s):
    print(s.p, s.q)
#calls the printname method on the instance x, 
#which prints the full name of the person, i.e., "tofaiel tota".
x = Student ("tofaiel", 'tota')

# This line calls the printname method on the instance x, which prints the full name of the person, i.e., "tofaiel tota".
x.printname()

'''

'''
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  pass
x = Student("mike","olsen")
x.printname()

'''
 #We want to add the __init__() function to the child class (instead of the pass keyword).
'''

class Person:
  def __init__(self, fname, lname):
     self.firstname = fname
     self.lastnmae = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def__init__(self, fname, lname):
    Person.__init__(self, fname, lname)
x = Student("salman", "Faesi")
x.printname()

'''
'''
txt = "We have {:<9} chickens."
print(txt.format(49))

t = "we love {:<6} Bangladesh."
print(t.format(70))
t = "we love  {:<3} Bangladesh."
print(t.format(30))

'''

'''
def say_hi(name, age):
    print("Hello " + name +",you are"+age)
    say_hi("mike", "35")
    say_hi("john", " 70")

    '''

def say_hi(name, age):
    print("Hello " + name + ", you are " + age)

say_hi("mike", "35")
say_hi("john", "70")




