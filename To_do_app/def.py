import turtle

def draw_cat():
    # Head
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()

    # Eyes
    turtle.penup()
    turtle.goto(-35, 0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(35, 0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    # Pupils
    turtle.penup()
    turtle.goto(-35, 10)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(6)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(35, 10)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(6)
    turtle.end_fill()

    # Nose
    turtle.penup()
    turtle.goto(0, -20)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

    # Mouth
    turtle.penup()
    turtle.goto(-20, -40)
    turtle.pendown()
    turtle.setheading(315)
    turtle.circle(20, 150)

    # Body
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.setheading(0)
    turtle.begin_fill()
    turtle.circle(100, 90)
    turtle.forward(180)
    turtle.circle(100, 90)
    turtle.forward(180)
    turtle.end_fill()

    # Legs
    turtle.penup()
    turtle.goto(-40, -180)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(50)

    turtle.penup()
    turtle.goto(40, -180)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(50)

    # Tail
    turtle.penup()
    turtle.goto(180, -100)
    turtle.pendown()
    turtle.setheading(60)
    turtle.circle(80, 120)

    turtle.hideturtle()
    turtle.done()

# Main function
def main():
    draw_cat()

if __name__ == "__main__":
    main()
  