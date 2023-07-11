from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('blue')
        self.restart()

    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def move_left(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 10
        self.goto(new_x, self.ycor())

    def restart(self):
        self.goto(0, -280)
        self.setheading(90)