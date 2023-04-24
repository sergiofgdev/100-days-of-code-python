from paddle import Paddle


class PlayerTwo(Paddle):
    def __init__(self):
        super(PlayerTwo, self).__init__()
        self.goto(-300, 0)
