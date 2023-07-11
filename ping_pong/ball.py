from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('yellow')
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.07

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_on_wall(self):
        self.y_move *= -1

    def bounce_on_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.8

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_on_paddle()
        self.move_speed = 0.1
