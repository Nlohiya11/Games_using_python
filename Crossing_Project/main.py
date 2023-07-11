from turtle import Screen
import time
from player import Player
from obstacle import Obstacle
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title("Turtle Crossing")
screen.tracer(0)


turtle = Player()

wall = Obstacle()
level = Scoreboard()


screen.listen()
screen.onkeypress(key="Up", fun=turtle.move_up)
screen.onkeypress(key="Left", fun=turtle.move_left)
screen.onkeypress(key="Right", fun=turtle.move_right)

game_on = True
while game_on:
    time.sleep(0.05)
    screen.update()

    wall.walls()
    wall.move_obstacle()
    if turtle.ycor() > 300:
        level.increase_score()
        turtle.restart()
        wall.speed()

    for obstacles in wall.all_obstale:
        if obstacles.distance(turtle) < 20:
            game_on = False
            level.game_over()

screen.exitonclick()