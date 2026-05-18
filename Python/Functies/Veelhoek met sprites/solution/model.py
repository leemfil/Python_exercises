import turtle

pen = turtle.Turtle()
pen.speed(0)


def teken_sprite(lengte):
    draaihoek = 360 / 8

    for _ in range(8):
        pen.forward(lengte)
        pen.backward(lengte)
        pen.left(draaihoek)


def teken_veelhoek(lengte, aantal_zijden):
    draaihoek = 360 / aantal_zijden
    lengte_sprite = lengte / 2

    for _ in range(aantal_zijden):
        teken_sprite(lengte_sprite)
        pen.forward(lengte)
        pen.left(draaihoek)


zijde = int(input("Geef de lengte van een zijde: "))
aantal = int(input("Geef het aantal zijden: "))

teken_veelhoek(zijde, aantal)

turtle.exitonclick()
