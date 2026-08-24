import turtle

pen = turtle.Turtle()
pen.speed(0)


def teken_sprite(aantal_beentjes):
    draaihoek = 360 / aantal_beentjes

    for _ in range(aantal_beentjes):
        pen.forward(50)
        pen.backward(50)
        pen.left(draaihoek)

    return "Sprite klaar."


eerste_sprite = int(input("Geef het aantal beentjes voor de eerste sprite: "))
tweede_sprite = int(input("Geef het aantal beentjes voor de tweede sprite: "))

print(teken_sprite(eerste_sprite))

pen.penup()
pen.forward(150)
pen.pendown()

print(teken_sprite(tweede_sprite))

turtle.exitonclick()
