global_variable = None

def modify_global():

    global global_variable

    global_variable = 'Hello Students'
    return 

modify_global()



# Define a global variable
global_variable = 0

# Define a function containing another function
def outer_function():
    # Define a function inside the outer function
    def inner_function():
        global global_variable
        global_variable += 1
        print("Inner function: Global variable incremented to", global_variable)
    
    print("Outer function: Calling inner function")
    inner_function()

# Call the outer function
outer_function()


