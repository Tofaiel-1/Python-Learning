master_pwd = input("What is the Master password?")
def view():
    with open("password.txt","a") as f:
        f.write(name +"|" pwd + "\n")
def add():
    name = input("Account name:")
    pwd = input("Password:")
    with open("password.txt","a") as f:
        f.write(name +"|" pwd + "\n")
while True:
    mode = input("Would you like to add anew password or existing ones(view ,add)? or press q quit")
    if mode == "q":
        break
if mode == 'View':
    pass 
elif mode =="q
if ":