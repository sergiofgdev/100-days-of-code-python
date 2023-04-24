import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("black")
tim.pensize(1)

# Cambiar el color
turtle.colormode(255)


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.color(r, g, b)


# todo Cuadrado
# for num in range(4):
#     tim.speed(2)
#     tim.pensize(5)
#     tim.forward(100)
#     tim.right(90)
#

# todo Linea discontinua
# Cambiando el color
# for n in range(20):
#     tim.color("black")
#     tim.forward(20)
#     tim.color("white")
#     tim.forward(20)

# Levantando el boli
# for n in range(20):
#     tim.pendown()
#     tim.forward(20)
#     tim.penup()
#     tim.forward(20)

# todo triangulo, cuadrado, pentagono, hexagono, heptagono, octogono, noneagono, decagono
# todo Dividir 360 entre 3, 4, 5, 6, 7, 8, 9, 10]
# Dibujar las formas
# def draw_shape(number_sides):
#     for _ in range(number_sides):
#         angulo = 360/number_sides
#         tim.fd(100)
#         tim.right(angulo)
#
#
# for n in range(3, 100):
#     change_color()
#     draw_shape(n)

# todo Random Walk

# Mi metodo
# action_list_move = [tim.fd, tim.bk]
# action_list_turn = [tim.right, tim.left]
#
# for n in range(1000):
#     random.choice(action_list_move)(20)
#     change_color()
#     random.choice(action_list_turn)(90)
#     change_color()


# directions = [0, 90, 180, 270]
# for n in range(500):
#     change_color()
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


# todo espirografo circular

tim.speed("fastest")


# size_gap es el espaciado que va a haber entre cada circulo
def draw_spiro(size_gap):
    for n in range(int(360 / size_gap)):
        change_color()
        tim.circle(100)
        tim.setheading(tim.heading() + size_gap)


draw_spiro(2)

screen = turtle.Screen()
screen.exitonclick()
