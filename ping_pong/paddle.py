from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.goto(position)

    def move_up(self):
        new_u = self.ycor() + 20
        if new_u <= 265:
            self.goto(self.xcor(), new_u)

    def move_down(self):
        new_d = self.ycor() - 20
        if new_d <= -265:
            self.goto(self.xcor(), new_d)
