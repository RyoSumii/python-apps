from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 5
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.seth(90)
        self.go_to_start()

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def reach_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
