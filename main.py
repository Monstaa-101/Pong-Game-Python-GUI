from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from boundary import Boundary
from scoreboard import *

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
boundary = Boundary()
boundary.upBound()
boundary.downBound()
boundary.rightBound()
boundary.leftBound()

left_scoreboard = Scoreboard()
ratio_scoreboard = Scoreboard()
right_scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")


game_is_on = True
while(game_is_on):
    time.sleep(ball.move_speed)
    screen.update()
    boundary.title("PONG GAME",0,200)
    ball.move()
    ratio_scoreboard.ratio_diff(0,120)

    if (ball.ycor()>270 or ball.ycor()< -270):
        ball.bounce()

    if (ball.xcor() == r_paddle.xcor()-10 and (r_paddle.ycor()-42<ball.ycor()<r_paddle.ycor()+42)):
        ball.hit()

    if (ball.xcor() == l_paddle.xcor()+10 and l_paddle.ycor()-42<ball.ycor()<l_paddle.ycor()+42):
        ball.hit()

    if left_scoreboard.l_score == 0:
        left_scoreboard.show_score(-60,120)
    if(ball.xcor()<-380):
        ball.l_reset_position()
        ball.move()
        right_scoreboard.plus_point()
        right_scoreboard.clear()
        right_scoreboard.show_score(60, 120)

    if  right_scoreboard.l_score == 0:
        right_scoreboard.show_score(60,120)
    if(ball.xcor()>380):
        ball.r_reset_position()
        ball.move()
        left_scoreboard.plus_point()
        left_scoreboard.clear()
        left_scoreboard.show_score(-60, 120)


screen.exitonclick()