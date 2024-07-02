def file_writing():

    with open('files.txt',"w") as f:

        n = input('Enter your name: ')

        d = input("Enter your faculty name: ")

        m = ['cse', 'ag', 'bba', 'nfs', 'esdm', 'lla', 'ansvm']

        d = d.upper() and d.lower()

        if d in m:

            f.write(f"Welcome {n} to Basic Programming with python course ")

        else:
            f.write(f" Ops! Faculty doesn't match! ")

def file_reading():

    with open("files.txt" , "r") as f:
        x = f.read()
        print(x)

file_writing()
file_reading()