from turtle import Turtle, Screen
from paddle import Paddle
from player_one import PlayerOne
from player_two import PlayerTwo

game_is_on = True

# Screen

# Screen
screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("Pong Game")
# screen.tracer(0)
screen.listen()


paddle = Paddle()
# playerOne = PlayerOne()
# playerTwo = PlayerTwo()

screen.exitonclick()
