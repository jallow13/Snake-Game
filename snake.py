from multiprocessing.resource_tracker import unregister
import random
from turtle import Turtle
X = [(0,0), (-20,0), (-40,0)]
STEPS_MOVED = 20
COLORS = ['white', 'red', 'yellow', 'green', 'blue', 'pink', 'purple',  'orange']
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.turtles_list = []
        self.create_snake()
        self.head = self.turtles_list[0]
    def create_snake(self):
        for turtle_ in X:
            self.add_segment(turtle_)

    def add_segment(self,position):
        new_turtle = Turtle()
        new_turtle.shape("circle")
        new_turtle.color(random.choice(COLORS))
        new_turtle.penup()
        new_turtle.goto(position)
        self.turtles_list.append(new_turtle)
    def extend(self):
        self.add_segment(self.turtles_list[-1].position())

    def move(self):
        for turtle in range(len(self.turtles_list) - 1, 0, -1):
            new_x = self.turtles_list[turtle - 1].xcor()
            new_y = self.turtles_list[turtle - 1].ycor()
            self.turtles_list[turtle].goto(x=new_x, y=new_y)
        self.head.forward(STEPS_MOVED)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)