from random import randint, choice
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """Models the group of cars and controls its creation and movement."""
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Creates new car and sets it at the starting position."""
        new_car = Turtle("square")
        new_car.color(choice(COLORS))
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        new_car.goto(300, randint(-250, 250))
        self.cars.append(new_car)

    def move_cars(self):
        """Makes all cars move forward, and deletes any that
          has reached the other edge of the screen."""
        for index, car in enumerate(self.cars):
            car.forward(self.car_speed)
            if car.xcor() < -320:
                self.cars.pop(index)

    def increase_speed(self):
        """Increases the moving speed of the cars."""
        self.car_speed += MOVE_INCREMENT

    def detect_collision(self, turtle):
        """Detects if any of the cars has collided
        with the turtle"""
        for car in self.cars:
            if car.distance(turtle) < 20:
                return True

        return False
