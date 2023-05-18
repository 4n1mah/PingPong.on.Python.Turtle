from turtle import Screen
from paddle import Paddle, center_line
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('Pong')
screen.tracer(0)

scoreboard = ScoreBoard()
ball = Ball()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
center_line()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
velocity = 0

game_on = True
while game_on:
    time.sleep(ball.move_speed[velocity])
    screen.update()
    ball.move_ball()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with right paddle

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        velocity += 1

    # collision with left paddle

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        velocity += 1
    # when right paddle misses

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        velocity = 0

    # when left paddle misses

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        velocity = 0

screen.exitonclick()
