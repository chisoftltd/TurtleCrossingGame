from turtle import Screen
from player import Player
from carmanager import CarManager
# from scoreboard import Scoreboard
import time
import random

#   Setup environment
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_list = []
player = Player()
for carposition in range(-50, 50, 10):
    carmanager = CarManager(carposition)
    car_list.append(carmanager)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    player.move_turtle()
    #carmanager.move_car(random.randint(0, len(car_list) - 1))
    car_list[random.randint(0, len(car_list) - 1)].move_car()

screen.exitonclick()
