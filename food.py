import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self, color, scale):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("circle")
        self.color(color)
        self.shapesize(stretch_len=scale, stretch_wid=scale)
        self.random_location()

    def random_location(self):
        ran_x = random.randint(-280, 270)
        ran_y = random.randint(-280, 270)
        self.goto(x=ran_x, y=ran_y)

    def create_food(self):
        pass
        #print(self.c)


