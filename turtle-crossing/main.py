import time
from turtle import Screen, listen, onkey, onkeypress
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle  = Player()
scoreboard = Scoreboard()
listen()
game_is_on = True
onkeypress(turtle.move_up,"Up")
onkeypress(turtle.move_down,"Down")

cars = CarManager()

while game_is_on:
    time.sleep(0.1)
    
    cars.movement()    
    if turtle.ycor() == 270:
        scoreboard.scored()
    screen.update()
    
