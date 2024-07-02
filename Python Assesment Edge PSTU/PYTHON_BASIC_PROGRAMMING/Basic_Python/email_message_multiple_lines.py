fullname = input('Please Enter your full name for a greeting message: ')
course = input('Please Enter your course name: ')
message = '''Hi! {}
 Thank you for attending EDGE's beginner {}  course  ''' . format(fullname, course)
print(message)
