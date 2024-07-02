
# def file_writing():

#     with open('files.txt',"w") as f:

#         n = input('Enter your name: ')

#         d = input("Enter your faculty name: ")

#         if d.lower() or d.upper() == 'cse' or d.lower() or d.upper() == 'agriculture' and d.lower() or d.upper() == 'fisheries':

#             f.write(f"Welcome {n} to Basic Programming with python course ")
#         else:

#             f.write(f"Welcome {n} to MS Word Exel Course.")

def file_reading():

    with open("files.txt" , "r") as f:
        x = f.read()
        print(x)

#file_writing()
file_reading()

        
        