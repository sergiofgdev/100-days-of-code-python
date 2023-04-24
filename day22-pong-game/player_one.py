from paddle import Paddle


class PlayerOne(Paddle):

    def __init__(self):
        super(PlayerOne, self).__init__()
        self.goto(300, 0)

    def movement(self):
        self.listen()
        self.onkey(self.up, "Up")
        self.onkey(self.down, "Down")
        self.onkey(self.left, "Left")
        self.onkey(self.right, "Right")
