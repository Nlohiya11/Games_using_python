import random
from turtle import Turtle, Screen
import time
import pandas

def move_right():
    if snake_body[0].heading() != 180:
        snake_body[0].speed(0)
        snake_body[0].setheading(0)
        snake_body[0].speed(1)


def move_up():
    if snake_body[0].heading() != 270:
        snake_body[0].speed(0)
        snake_body[0].setheading(90)
        snake_body[0].speed(1)


def move_down():
    if snake_body[0].heading() != 90:
        snake_body[0].speed(0)
        snake_body[0].setheading(270)
        snake_body[0].speed(1)


def move_left():
    if snake_body[0].heading() != 0:
        snake_body[0].speed(0)
        snake_body[0].setheading(180)
        snake_body[0].speed(1)


def listen_to_command(n):
    n.listen()
    n.onkey(key="Up", fun=move_up)
    n.onkey(key="Left", fun=move_left)
    n.onkey(key="Right", fun=move_right)
    n.onkey(key="Down", fun=move_down)


def new_screen(n):
    n.bgcolor('black')
    n.setup(width=700, height=720)
    n.title(titlestring="Snake Game")
    n.textinput(title="welcome to the Snake Game", prompt=f'''Instructions :-
Up arrow - move up, Down arrow - move down
Left arrow - move left, Right arrow - move right

Press any key to Start''')


def snake_food(a):
    a.hideturtle()
    a.speed(0)
    a.shape('circle')
    a.shapesize(0.5, 0.5, 0.5)
    a.color('yellow')
    random_xcor = random.randint(-320, 320)
    random_ycor = random.randint(-320, 320)
    a.penup()
    a.setx(random_xcor)
    a.sety(random_ycor)
    a.showturtle()


def add_new_snake():
    trio = (snake_body[-1].position())
    snake1 = Turtle()
    snake1.penup()
    snake1.shape('square')
    snake1.color('silver')
    snake1.goto(trio)
    snake_body.append(snake1)


def wall_building():
    wall = Turtle()
    wall.hideturtle()
    wall.pensize(40)
    wall.color('dark red')
    wall.penup()
    wall.goto(-350, 350)
    wall.speed(0)
    wall.pendown()
    wall.goto(-350, -350)
    wall.goto(350, -350)
    wall.goto(350, 350)
    wall.goto(-350, 350)
    wall.showturtle()


scores = Turtle()


def scoreboard():
    scores.hideturtle()
    scores.penup()
    scores.color('white')
    scores.goto(0, 330)
    scores.write(f"Score = {score} Highest Score = {high_score}", align="center", font=("Arial", 20, "normal"))


def update_score():
    scores.reset()
    highest_score()
    scoreboard()


def eating_body():
    ycor_snake = []
    xcor_snake = []
    for square in snake_body:
        square_ycor = square.ycor()
        ycor_snake.append(square_ycor)
    for square in snake_body:
        square_xcor = square.xcor()
        xcor_snake.append(square_xcor)
    for n in range(2, len(snake_body)):
        if head.xcor() == xcor_snake[n]:
            if head.ycor() == ycor_snake[n]:
                screen.reset()


def highest_score():
    if score > high_score:
         with open("snake_highest.txt", mode="w") as file:
                file.write(f"{score}")


is_continue = True
while is_continue:
    with open("snake_highest.txt", mode="r") as file:
        inti = file.read()
    high_score = int(inti)
    time.sleep(0)
    snake_body = []
    screen = Screen()
    new_screen(screen)
    wall_building()
    score = 0
    screen.tracer(0)
    initial_position = [(0, 0), (-20, 0), (-40, 0)]
    for position in initial_position:
        snake = Turtle()
        snake.penup()
        snake.shape('square')
        snake.color('silver')
        snake.goto(position)
        snake_body.append(snake)

    difficulty = screen.numinput(title="Difficulty level", prompt='''Press 1 for Easiest Speed, 2 for Easy Speed,
    Press 3 for Medium Speed,
    Press 4 for Hard Speed, Press 5 for Hardest speed''')
    if difficulty == 1:
        speed = 0.2
    elif difficulty == 2:
        speed = 0.15
    elif difficulty == 3:
        speed = 0.1
    elif difficulty == 4:
        speed = 0.06
    elif difficulty == 5:
        speed = 0.02
    else:
        speed = 0.1
    listen_to_command(screen)
    prey = Turtle()
    snake_food(prey)
    is_on = True
    scoreboard()
    while is_on:
        screen.update()
        time.sleep(speed)
        for num in range(len(snake_body) - 1, 0, -1):
            xcor_first = snake_body[num - 1].xcor()
            ycor_first = snake_body[num - 1].ycor()
            snake_body[num].goto(xcor_first, ycor_first)
        snake_body[0].forward(20)
        head = snake_body[0]
        if prey.xcor() - 15 < head.xcor() < prey.xcor() + 15 and prey.ycor() - 15 < head.ycor() < prey.ycor() + 15:
            prey.reset()
            snake_food(prey)
            score += 1
            scores.clear()

            update_score()
            add_new_snake()
            time.sleep(0)

        if head.xcor() > 330 or head.xcor() < -330:

            screen.reset()
            is_on = False

        elif head.ycor() > 330 or head.ycor() < -330:
            screen.reset()
            is_on = False
        eating_body()
    screen1 = Screen()
    choice = screen1.textinput(title=f"welcome to the Snake Game", prompt=f'''Your Score is : {score} highest_score = {high_score}

Press y to play again
If you want to quit Press ENTRE and click on screen''')
    if choice == "y":
        is_on = True
    else:
        screen1.reset()
        is_continue = False

screen.exitonclick()
