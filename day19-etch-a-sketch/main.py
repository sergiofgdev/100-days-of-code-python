from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()

# Funciones para moverse


def move_forward():
    tim.forward(10)


def move_backward():
    tim.back(10)


def move_clockwise():
    tim.right(10)


def move_counter_clockwise():
    tim.left(10)


def reset():
    tim.reset()


# Teclado


screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=move_clockwise, key="d")
screen.onkey(fun=move_counter_clockwise, key="a")
screen.onkey(fun=reset, key="c")

screen.exitonclick()


