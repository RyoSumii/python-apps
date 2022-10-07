import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()

    car.random_create()
    car.move()

    # 車との接触を検知
    for c in car.r_cars:
        if c.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    for c in car.l_cars:
        if c.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.reach_finish_line():
        player.go_to_start()
        car.increase_speed()
        scoreboard.level_up()

screen.exitonclick()
