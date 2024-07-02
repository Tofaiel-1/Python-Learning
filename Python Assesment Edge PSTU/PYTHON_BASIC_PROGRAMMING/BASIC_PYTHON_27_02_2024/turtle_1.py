from turtle import Turtle, bgcolor, circle, color, forward, left, right, speed


color('cyan')
bgcolor('black')
speed(11)
right(45)

for n in range(150):
    if 7 < n < 62:
        left(5)
    if 80 < n < 133:
        right(5)
    circle(30)
    if n < 80:
        forward(10)
    else:
        forward(5)


