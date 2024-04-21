import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.forward, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.generate_cars()
    car_manager.move_cars()
    if player.turtle.ycor() > 280:
        player.turtle.goto(0, -280)
        scoreboard.score += 1
        car_manager.i += 1
        scoreboard.update_scoreboard()
    for car in car_manager.car_list:
        if -40 < car.xcor() - player.turtle.xcor() < 40 and -20 < car.ycor() - player.turtle.ycor() < 20:
            scoreboard.game_over()
            game_is_on = False
    screen.update()

screen.exitonclick()
