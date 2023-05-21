import time
import turtle
from turtle import Screen,write
import  snake as sn
import food as fd
from controls import *

def end_game():
    screen.clearscreen()
    screen.bgcolor("black")
    turtle.color("white")
    turtle.write("GAME OVER", align="center", font=("Grumpy", 30, "bold"))
    turtle.penup()
    turtle.goto(x=0, y=-25)
    turtle.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

    turtle.hideturtle()

# Creating the Screen

screen = Screen()
screen.tracer(0)
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")

is_game_on = True

# Creating Snake, food,screen, speed

snake = sn.Snake()
food = fd.Food()
head = snake.body[0]
score = 0
speed = 0.1


screen.listen()
screen.onkey(key="Up",fun=snake.move_up)
screen.onkey(key="Down",fun=snake.move_dn)
screen.onkey(key="Left",fun=snake.move_left)
screen.onkey(key="Right",fun=snake.move_right)



while is_game_on:

    snake.move()
    screen.update()
    time.sleep(speed)

# Print the score in the game

    turtle.clear()
    turtle.penup()
    turtle.goto(x=0,y=270)
    turtle.color("white")
    turtle.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))
    turtle.hideturtle()


# This detects collision with food

    if collision(head,food.food):
        food.change_loc()
        snake.increase_body()
        score +=1
        if score % 5 == 0:
            speed -= 0.01


# This detects collision with wall

    if wall(head):
        is_game_on = False
        end_game()

    if snake.body_collision():
        is_game_on = False
        end_game()






















screen.exitonclick()