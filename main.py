import time
from turtle import Screen ,Turtle
from snake import Snake
from food import Food
from scores import ScoreBord

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBord()

screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Detect collision with Food
    if snake.head.distance(food) < 15:
        food.random_location()
        snake.extend()
        score.increase_s()
    #Detect collision with Wall
    if snake.head.xcor() < -300 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        is_game_on = False
        score.game_over()

    for seg in snake.turtles_list[1:]:
        if snake.head.distance(seg) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()