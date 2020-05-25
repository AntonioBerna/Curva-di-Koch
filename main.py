import turtle as t

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
if iterazione == "":
    iterazione = 4
else:
    iterazione = int(iterazione)

t.penup()
t.backward(lunghezza/2)  # spostamento penna
t.pendown()

for i in range(3):
    koch(lunghezza, iterazione)
    t.right(120)

t.mainloop()
