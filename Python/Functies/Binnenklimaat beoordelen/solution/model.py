def vraag_temperatuur():
    while True:
        try:
            temperatuur = float(input())
            return temperatuur
        except ValueError:
            print("Dat is geen geldige temperatuur.")


def vraag_luchtvochtigheid():
    while True:
        try:
            luchtvochtigheid = int(input())

            if luchtvochtigheid < 0 or luchtvochtigheid > 100:
                print("De luchtvochtigheid moet tussen 0 en 100 liggen.")
            else:
                return luchtvochtigheid

        except ValueError:
            print("Dat is geen geldige luchtvochtigheid.")


def beoordeel_klimaat(temperatuur, luchtvochtigheid):
    if temperatuur < 18:
        return "Het is te koud."
    elif temperatuur >= 24 and luchtvochtigheid >= 70:
        return "Het is warm en vochtig."
    elif temperatuur >= 24:
        return "Het is warm."
    elif luchtvochtigheid < 30:
        return "De lucht is te droog."
    elif luchtvochtigheid > 60:
        return "De lucht is vochtig."
    else:
        return "Het binnenklimaat is aangenaam."


temperatuur = vraag_temperatuur()
luchtvochtigheid = vraag_luchtvochtigheid()

print(beoordeel_klimaat(temperatuur, luchtvochtigheid))
