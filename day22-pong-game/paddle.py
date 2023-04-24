from turtle import Turtle, Screen


class Paddle(Turtle, Screen):

    def __init__(self):
        super(Paddle, self).__init__()
        self.penup()
        self.color("black")
        self.shape("square")
        self.shapesize(3, 1, 6)
        self.goto(300, 0)
        self.tracer(0)
