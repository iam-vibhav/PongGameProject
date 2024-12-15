from ball import Ball
import turtle as t
import time
from centreline import CentreLine
from paddle import Paddle
from scoreboard import ScoreBoard

screen = t.Screen()
screen.bgcolor("black")
screen.setup(1000, 600)
screen.title("Pong Game")


screen.tracer(0)
score = ScoreBoard()

centre_line = CentreLine()
left_user = Paddle()
left_user.goto(-480, 0)
right_user = Paddle()
right_user.goto(480, 0)

screen.tracer(1)

screen.listen()
screen.onkey(right_user.go_up, "Up")
screen.onkey(right_user.go_down, "Down")
screen.onkey(left_user.go_up, "w")
screen.onkey(left_user.go_down, "s")


ball = Ball()
game_is_on = True
while game_is_on:
    time.sleep(0.05)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    if (ball.distance(right_user) < 50 and ball.ycor() < 460) or (ball.distance(left_user) < 50 and ball.ycor() > -460):
        ball.bounce_paddle()

    if ball.xcor() > 500:
        screen.tracer(0)
        score.l_point()
        ball.goto(0, 0)
        screen.tracer(1)

    if ball.xcor() < -500:
        screen.tracer(0)
        score.r_point()
        ball.goto(0, 0)
        screen.tracer(1)

screen.exitonclick()




