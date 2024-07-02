n = 1

while n < 11:
    print(n)
    n = n + 1



Food = ('Breakfast', 'Launch', 'Supper', 'Dinner', 'Buffet')

students = {'name': 'Ameer', 'Id': 1, 'Batch': 'Python'}

food = {'Abeer ', 'Ameer ', 'Sadi ', 'Bin ', 'Bashar', 'S. M.'}

for f in food:
    print(f)

#How to change values inside a dict
students = {'name': 'Ameer', 'Id': 1, 'Batch': 'Python'}

# Change the value of the key 'Batch'
students['Batch'] = 'Data Science'

print(type(students['Batch']))

print(students)

#for key in students:
    #value = students[key]
    #print(f'{key} : {value}')




#for key, value in students.items():
    #print(f'{key}: {value}')


students = {'name': 'Ameer', 'Id': 1, 'Batch': 'Python'}

# Using del keyword
del students['Batch']

# Using pop() method
students.pop('Id')

print(students)



#Adding key value pairs
students = {'name': 'Ameer', 'Id': 1, 'Batch': 'Python'}

# Updating a value
students['Batch'] = 'Data Science'

students['Address'] = 'Patuakhlai'

# Adding a new key-value pair
students['Grade'] = 'A'

# Using update() method to add multiple key-value pairs
students.update({'Age': 25, 'Gender': 'Male'})
#Using pop function
students.pop('Address')
print(students)
