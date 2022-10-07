from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(object):
    def __init__(self):
        self.r_cars = []
        self.l_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.create_car()
        self.car_side = [1, -1]

    def random_create(self):
        num = random.randint(0, 10)
        if num <= 2:
            self.create_car()

    def create_car(self):
        car = Turtle("square")
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        random_num = random.randint(0, 1)
        if random_num == 0:
            car.goto(300, random.randint(-250, 250))
            self.r_cars.append(car)
        else:
            car.goto(-300, random.randint(-250, 250))
            self.l_cars.append(car)

    def move(self):
        for car in self.r_cars:
            car.goto(car.xcor() - self.move_distance, car.ycor())
        for car in self.l_cars:
            car.goto(car.xcor() + self.move_distance, car.ycor())

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
