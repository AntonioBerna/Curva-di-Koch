import turtle as t

def controllo_input(iterazione):
    if iterazione == "":
        iterazione = 4
    else:
        iterazione = int(iterazione)

    return iterazione

def move():
    t.penup()
    t.backward(lunghezza / 2)  # spostamento penna
    t.pendown()


def fiocco_di_neve_koch(lunghezza, iterazione):
    for i in range(3):
        koch(lunghezza, iterazione)
        t.right(120)


def koch(lunghezza, iterazione):
    if iterazione == 0:
        t.forward(lunghezza)
    else:
        lunghezza /= 3
        koch(lunghezza, iterazione-1)
        t.left(60)
        koch(lunghezza, iterazione - 1)
        t.right(120)
        koch(lunghezza, iterazione - 1)
        t.left(60)
        koch(lunghezza, iterazione - 1)


bob = t.Turtle()

t.speed(0)  # velocità max
lunghezza = 300
iterazione = input("Inserisci il numero di iterazioni della curva di Koch (default -> 4): ")
iterazione = controllo_input(iterazione)

move()
fiocco_di_neve_koch(lunghezza, iterazione)

t.mainloop()
