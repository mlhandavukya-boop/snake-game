from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
screen=Screen()
food=Food()
score=ScoreBoard()
game_over=Turtle()
screen.title("SNAKE GAME")
screen.bgcolor("black")
screen.tracer()
screen.setup(width=600,height=600)
score.score_addition()

tini_snake=Snake()
tini_snake.snakes_object()
screen.listen()
screen.onkey(tini_snake.move_right,"Right")
screen.onkey(tini_snake.move_up,"Up")
screen.onkey(tini_snake.move_down,"Down")
screen.onkey(tini_snake.move_left,"Left")
game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    tini_snake.move()
    if tini_snake.head.distance(food)<15:
        food.collision()
        tini_snake.extend()
        score.score_addition()
    if tini_snake.head.xcor()>280 or tini_snake.head.xcor()<-280 or tini_snake.head.ycor()>280 or tini_snake.head.ycor()<-280:
        score.reset()
        tini_snake.reset_game()
    for segment in tini_snake.snake_list[1:]:
        if tini_snake.head.distance(segment)<10:
            score.reset()
            tini_snake.reset()
screen.exitonclick()