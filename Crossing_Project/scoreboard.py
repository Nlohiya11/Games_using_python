from turtle import Turtle

with open("new_file.txt", mode="r") as file:
    inti = file.read()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 1
        self.high_score = int(inti)
        self.goto(-2, 250)
        self.write(f"Level  :  {self.score} High Score : {self.high_score}", align="center", font=("Arial", 20, "normal"))
        self.update_score()

    def update_score(self):
        self.clear()
        self.highest_score()
        self.write(f"Level  :  {self.score} High Score : {self.high_score}", align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0, 20)
        self.write(f"  GAME OVER\n\n Your Score is : {self.score}", align="center", font=("Arial", 20, "normal"))
        self.highest_score()
        self.goto(0, -40)
        self.write(f"Highest Score is : {self.high_score}", align="center", font=("Arial", 20, "normal"))

    def highest_score(self):
        if self.score > self.high_score:
            with open("new_file.txt", mode="w") as file:
                file.write(f"{self.score}")

