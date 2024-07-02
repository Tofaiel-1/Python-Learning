global_variable = 0

def change_global_variable():

    global global_variable

    global_variable += 1

    print(f'''
          
          We are accessing a global variable inside our Function.
          
          Value has incremented to {global_variable}

        ''')



change_global_variable()





