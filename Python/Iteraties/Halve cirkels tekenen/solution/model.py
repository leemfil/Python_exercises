import turtle

pen = turtle.Turtle()
pen.speed(3)

pen.circle(50, 180)
pen.penup()
pen.left(180)
pen.forward(100)
pen.left(180)
pen.pendown()
pen.circle(50, 180)

turtle.exitonclick()
