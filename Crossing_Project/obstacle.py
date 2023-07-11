
from turtle import Turtle
from random import randint
distance = 5


class Obstacle:

    def __init__(self):
        self.all_obstale = []
        self.car_speed = distance

    def walls(self):
        chance_of_getting_wall = randint(1, 5)
        if chance_of_getting_wall == 1:
            obstacle = Turtle("square")
            size_of_obstacle = randint(2, 4)
            obstacle.shapesize(1, size_of_obstacle)
            obstacle.penup()
            obstacle.color('red')
            random_y = 60*randint(-3, 3)
            obstacle.goto(400, random_y)
            self.all_obstale.append(obstacle)

    def move_obstacle(self):
        for obstacles in self.all_obstale:
            obstacles.backward(self.car_speed)

    def speed(self):
        self.car_speed += 4
