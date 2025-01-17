from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVING_DISTANCE = 10
FINISH_LIVE_Y = 270


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def up(self):
        self.forward(MOVING_DISTANCE)

    def reset_position(self):
        self.teleport(0, -280)
