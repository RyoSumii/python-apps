from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.color("White")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)

    def up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
