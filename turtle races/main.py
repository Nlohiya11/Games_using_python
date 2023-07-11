import random
from turtle import Turtle, Screen
vansh = Turtle()
nitin = Turtle()
oshan = Turtle()
ankit = Turtle()
harshit = Turtle()
hemant = Turtle()
screen = Screen()
screen.setup(width=720, height=340)
screen.bgcolor('black')
all_turtle = [vansh, ankit, nitin, oshan, hemant, harshit]
vansh.color('purple')
oshan.color('pink')
nitin.color('cyan')
ankit.color('navy')
harshit.color('green')
hemant.color('gold')
hemant.shape('turtle')
nitin.shape('turtle')
vansh.shape('turtle')
oshan.shape('turtle')
harshit.shape('turtle')
ankit.shape('turtle')
nitin.penup()
ankit.penup()
harshit.penup()
hemant.penup()
vansh.penup()
oshan.penup()
nitin.goto(-350, -30)
oshan.goto(-350, 10)
vansh.goto(-350, 50)
hemant.goto(-350, 90)
harshit.goto(-350, -70)
ankit.goto(-350, -110)
finish = Turtle()
finish.pensize(5)
finish.hideturtle()
finish.penup()
finish.speed(0)
finish.color('red')
finish.goto(325, 170)
for i in range(0, 17):
    finish.pendown()
    finish.setheading(270)
    finish.forward(10)
    finish.penup()
    finish.forward(10)

user_bet = screen.textinput(title="make you bet", prompt="vansh=purple, oshan=pink, nitin = cyan, ankit=navy, "
                                                         "harshit=green, hemant=gold..Chose your player?")


if user_bet:
    race_is_on = True
while race_is_on:
    for turtle in all_turtle:
        if turtle.xcor() > 300:
            winner_color = turtle.pencolor()
            if winner_color == "cyan":
                winner_player = "nitin"
            elif winner_color == "gold":
                winner_player = "hemant"
            elif winner_color == "green":
                winner_player = "harshit"
            elif winner_color == "navy":
                winner_player = "ankit"
            elif winner_color == "pink":
                winner_player = "oshan"
            elif winner_color == "purple":
                winner_player = "vansh"
            race_is_on = False
            if winner_player == user_bet:
                print(f"You have won the game!.. The winner of the race is {winner_player}")
            else:
                print(f"You have lost the game!.. The winner of the race is {winner_player}")
        distance = random.randint(0, 8)
        turtle.forward(distance)

screen.exitonclick()
