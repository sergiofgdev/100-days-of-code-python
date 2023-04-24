import random

import colorgram
from turtle import Turtle, Screen

colors = colorgram.extract('image.jpg', 6)
rbg_colors = []

for color in colors:
    r = color.rgb.r
    b = color.rgb.b
    g = color.rgb.g
    new_color = (r, b, g)
    rbg_colors.append(new_color)

# rbg_colors
color_list = [(229, 226, 228), (225, 224, 223), (199, 117, 175), (124, 24, 36), (210, 213, 221), (168, 57, 106)]

# todo Hirst painting

tim = Turtle()
tim.screen.colormode(255)

# method
y = 20
for _ in range(10):
    y += 20
    for n in range(10):
        c = random.choice(color_list)
        tim.pendown()
        tim.dot(20, c)
        tim.penup()
        tim.forward(50)
    y += 20
    tim.goto(0, y)



# Cerrar la ventana
screen = Screen()
screen.exitonclick()
