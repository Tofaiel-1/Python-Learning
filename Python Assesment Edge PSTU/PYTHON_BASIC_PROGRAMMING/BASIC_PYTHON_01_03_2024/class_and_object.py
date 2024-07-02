fresh = 'I feel Fresh!'
tired = 'I feel Tired!'

class Hours:
    def morning(self):
        print(fresh)
        
    def evening(self):
        print(tired)

# Creating an instance of Hours class
my_hours = Hours()

# Calling the morning method
my_hours.morning()  # Output: I feel Fresh!

# Calling the evening method
my_hours.evening()  # Output: I feel Tired!
