import random
from turtle import Turtle

class Food:
    def __init__(self):
        self.food = Turtle("circle")
        self.food.penup()
        self.food.color("red")
        self.food.shapesize(0.8)
        self.food.goto(random.randint(-280,280),random.randint(-280,280))

    def change_loc(self):
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        self.food.goto(x,y)

