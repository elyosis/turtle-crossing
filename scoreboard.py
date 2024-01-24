from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Models the scoreboard keeping track of status of the game."""
    level = 1

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-210, 250)
        self.update_board()

    def update_board(self):
        """Resets and updates board with latest score data."""
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        """Increases the game level by 1."""
        self.level += 1
        self.update_board()

    def game_over(self):
        """Sets a game over message."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
