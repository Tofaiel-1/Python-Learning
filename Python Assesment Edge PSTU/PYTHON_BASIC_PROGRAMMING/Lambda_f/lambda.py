add = lambda x , y : x + y

print( add( 6,  5 ) )



























numbers = [2, 3, 4, 5, 6, 7, 8]

squared = map(lambda x: x ** 2, numbers )

print(list(squared))


numbers = [1,2,3,4,5,6]

even = filter(lambda x : x % 3 == 0, numbers)

print(list(even))

from functools import reduce
numbers = [1,2,3,4,5]

product = reduce(lambda x, y: x * y, numbers)

print(product)


prices = [10, 20, 30]

total = 0
for price in prices:
    total += price

print(f'Total: {total}.')



#Nested Loops
for x in range(5):
    for y in range(4):
        print(f'{x}  {y}')


NUMBERS = [5, 2, 5, 2, 2]

for x_count in NUMBERS:
    print( 'X' * x_count)


for x_count in NUMBERS:
    output = ''
    for x in range(x_count):
        output += 'X'
    print(output)


class Point:
    def move(self):
        print('MOVE!')
    def draw(self):
        print("DRAW!")
point1 = Point()
point1.draw()



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def draw(self):
        print(f"Drawing point at ({self.x}, {self.y})")

point1 = Point(3, 4)
point1.move(2, 3)
point1.draw()

