from turtle import Turtle
import time
pos_n = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.body[0].color("red")

    def create_snake(self):
        for i in pos_n:
            t = Turtle("square")
            t.penup()
            t.color("white")
            t.goto(i)
            self.body.append(t)

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            x_cor = self.body[i - 1].xcor()
            y_cor = self.body[i - 1].ycor()
            self.body[i].goto(x=x_cor, y=y_cor)
        self.body[0].forward(MOVE_DISTANCE)

    def move_right(self):
        head = self.body[0]
        if int(head.heading()) == 180:
            pass
        else:
            head.setheading(0)
            time.sleep(0.01)

    def move_left(self):
        head = self.body[0]
        if int(head.heading()) == 0:
            pass
        else:
            head.setheading(180)
            time.sleep(0.01)

    def move_up(self):
        head = self.body[0]
        if int(head.heading()) == 270:
            pass
        else:
            head.setheading(90)
            time.sleep(0.01)

    def move_dn(self):
        head = self.body[0]
        if int(head.heading()) == 90:
            pass
        else:
            head.setheading(270)
            time.sleep(0.01)

    def increase_body(self):
        t = Turtle("square")
        t.penup()
        t.color("white")
        t.goto(x=self.body[len(self.body)-1].xcor()-20,y=self.body[len(self.body)-1].ycor()-20)
        self.body.append(t)

    def body_collision(self):
        for i in range(1,len(self.body)):
            if self.body[0].distance(self.body[i]) <10:
                return True