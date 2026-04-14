from turtle import Turtle

FONT=('Arial', 13, 'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as data:
            self.high_score=int(data.read())
        self.t=Turtle()
        self.t.penup()
        self.t.hideturtle()
        self.t.color("white")
        self.t.goto(0, 280)
        self.score=0
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"score:{self.score} high score:{self.high_score}",align="center",font=FONT)
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt", mode="w") as data:
                self.high_score = int(data.write(f"{self.high_score}"))
        self.score=0
        self.update_score()
    def score_addition(self):
        self.score+=1
        self.update_score()

