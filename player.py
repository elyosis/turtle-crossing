from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    """Models the turtle controlled by the player"""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset_position()

    def move(self):
        """Moves the turtle forward."""
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        """Sets the turtle back at its starting position."""
        self.goto(STARTING_POSITION)
