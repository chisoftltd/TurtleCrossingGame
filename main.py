from turtle import Screen
from player import Player
from carManager import CarManager
from scoreboard import Scoreboard
import time

#   Set up environment
screen = Screen()
screen.setup(width=800, height=800)
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()