from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_data()
        self.read_data()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.ht()
        self.goto(0, 270)

    def show_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.show_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_data()
        self.score = 0
        self.show_score()

    def read_data(self):
        with open("data.txt") as data:
            return int(data.read())

    def write_data(self):
        with open("data.txt", "w") as data:
            data.write(f"{self.high_score}")
