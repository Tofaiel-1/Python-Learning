
full_name = input('Give the name of your teacher to Judge As Good Or Average: ')

rating = float(input('Give Your rating to the teacher? '))  # Convert input to float

is_a_good_teacher = input('Give Your opinion to your teacher as Good or Average:  ')

def checkLength():
    global is_a_good_teacher  # Declare the variable as global

    if len(is_a_good_teacher) == 4:

        is_a_good_teacher = True

    elif len(is_a_good_teacher) == 7:

        is_a_good_teacher = False

        print(is_a_good_teacher)
    else:
        print(is_a_good_teacher)

    return is_a_good_teacher

checkLength()

if full_name == 'Chinmoy Bepary' and rating == 4.8 and is_a_good_teacher == 'Good':
    print(full_name + ' is a Perfect Teacher! and His rating is ' + str(rating))
elif full_name != 'Chinmoy Bepary' or rating != 4.8 or is_a_good_teacher != 'Good':  # Changed condition to OR
    print(full_name + ' is not a Perfect Teacher! and His rating is ' + str(rating))
else:
    print('Please input again!')
