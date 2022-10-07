from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.ht()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("courier", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def l_win(self):
        self.goto(-200, 0)
        self.write("You Win", align="center", font=("courier", 30, "normal"))
        self.goto(200, 0)
        self.write("You Lose", align="center", font=("courier", 30, "normal"))

    def r_win(self):
        self.goto(-200, 0)
        self.write("You Lose", align="center", font=("courier", 30, "normal"))
        self.goto(200, 0)
        self.write("You Win", align="center", font=("courier", 30, "normal"))
