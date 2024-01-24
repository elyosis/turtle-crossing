import time
from random import randint
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    new_car_chance = randint(1, 6)

    if new_car_chance == 1:
        car_manager.create_car()

    car_manager.move_cars()

    has_collided = car_manager.detect_collision(player)
    if has_collided:
        game_is_on = False
        scoreboard.game_over()

    if player.ycor() > 280:
        player.reset_position()
        scoreboard.increase_level()
        car_manager.increase_speed()


screen.exitonclick()
