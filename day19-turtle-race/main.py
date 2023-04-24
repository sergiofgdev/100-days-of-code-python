from turtle import Turtle, Screen
import random

screen = Screen()

# Pantalla
screen.setup(height=400, width=900)
apuesta = screen.textinput(title="Haz tu apuesta", prompt="Que tortuga ganara la carrera? Haz tu apuesta")


# Tortugas
colors = ("green", "red", "orange", "blue", "purple", "yellow")
y_position = [150, 100, 50, 0, -50, -100]
turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-380, y=y_position[turtle_index])
    new_turtle.color(colors[turtle_index])
    turtles.append(new_turtle)


# Empezar carrera
is_race = True

while is_race:
    for participant_turtle in turtles:
        turtle_position = participant_turtle.xcor()
        if turtle_position > 400:
            is_race = False
            winning_color = participant_turtle.pencolor()
            if apuesta == winning_color:
                print(f"Has ganado! La tortuga {winning_color} es la ganadora.")
            else:
                print(f"Has perdido! La tortuga {winning_color} es la ganadora.")

        participant_turtle.forward(random.randint(0, 10))


screen.exitonclick()
