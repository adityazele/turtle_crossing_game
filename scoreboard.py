from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard:

    def __init__(self):
        self.tim = Turtle()
        self.tim.hideturtle()
        self.tim.penup()
        self.tim.goto(-290, 260)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.tim.reset()
        self.tim.hideturtle()
        self.tim.penup()
        self.tim.goto(-290, 260)
        self.tim.write(f'Level {self.score}', True, font=FONT)

    def game_over(self):
        self.tim.goto(-60, 0)
        self.tim.write('Game Over', True, font=FONT)
