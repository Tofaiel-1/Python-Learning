import datetime
current_year = datetime.datetime.now().year
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year
print("You are", age, "years old.")
