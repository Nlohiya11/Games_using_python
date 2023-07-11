from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(1000, 600)
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((450, 0))
l_paddle = Paddle((-450, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.move_up)
screen.onkeypress(key="Down", fun=r_paddle.move_down)
screen.onkeypress(key="w", fun=l_paddle.move_up)
screen.onkeypress(key="s", fun=l_paddle.move_down)
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 265 or ball.ycor() < -265:
        ball.bounce_on_wall()

    if ball.distance(r_paddle) < 55 and ball.xcor() > 420 or ball.distance(l_paddle) < 50 and ball.xcor() < -420:
        ball.bounce_on_paddle()

    if ball.xcor() > 450:
        ball.reset_position()
        ball.move()
        scoreboard.l_score += 1
        scoreboard.update_score()
    elif ball.xcor() < -450:
        ball.reset_position()
        ball.move()
        scoreboard.r_score += 1
        scoreboard.update_score()


screen.exitonclick()
