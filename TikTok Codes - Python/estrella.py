import turtle
import time

screen = turtle.Screen()

turt = turtle.Turtle()

tamanio = 100

for i in range(8):
    if i<4:
        for j  in range(5):
            turt.forward(tamanio)
            turt.right(144)
        turt.pu()
        turt.forward(100)
        turt.down()
    else:
        if i ==4:
            turt.pu()
            turt.forward(-400)
            turt.down()
        for j in range(5):
            turt.forward(-tamanio)
            turt.right(-144)
        turt.pu()
        turt.forward(-100)
        turt.down()
time.sleep(5)