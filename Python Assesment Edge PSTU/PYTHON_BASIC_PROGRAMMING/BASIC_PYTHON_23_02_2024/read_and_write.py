with open("file.txt", "w") as f:
    f.write('Sadi')

with open("file.txt", "r") as f:
    data = f.read()
    print(data)
