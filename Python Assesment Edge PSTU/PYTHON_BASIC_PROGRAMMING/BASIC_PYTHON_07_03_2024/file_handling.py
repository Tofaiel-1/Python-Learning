
'''def file_writing():

    with open('files.txt' , "w") as f:

        n = input('Enter your name: ')

        d = input("Enter your faculty name: ")

        d = d.upper()

        if d == 'CSE' or 'AGRICULTURE' or 'FISHERIES' and 'CSE' or 'AGRICULTURE' or 'FISHERIES' not in d:
            
                f.write(f"Welcome {n} to Basic Programming with python course ")
        else:
            print('Input Correct Department Name')

        
        

def file_reading():

    with open("files.txt" , "r") as f:

        x = f.read()

        print(x)

file_writing()
file_reading()'''


def file_writing():

    with open('files.txt',"w") as f:

        n = input('Enter your name: ')

        d = input("Enter your faculty name: ")
        


        if  d == 'cse'  or d == 'agriculture' or d == 'fisheries' in d.upper():

            if "CSE" or "AGRICULTURE" or "FISHERIES" in d:

                f.write(f"Welcome {n} to Basic Programming with python course ")
            else:
                print('Not in d!')

        else:

            f.write(f"Welcome {n} to MS Word Exel Course.")

def file_reading():

    with open("files.txt" , "r") as f:
        x = f.read()
        print(x)

file_writing()
file_reading()
