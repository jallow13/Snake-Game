import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.random_location()
    def random_location(self):
        ran_x = random.randint(-280, 270)
        ran_y = random.randint(-280, 270)
        self.goto(x=ran_x, y=ran_y)