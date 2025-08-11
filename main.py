from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
# For r_paddle movement
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
# For l_paddle movement
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

game_on = True
while game_on:
    time.sleep(0.1 )
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) <50 and ball.xcor() < -320:
        ball.bounce_x()
    # if the ball missed by r_player
    if ball.xcor() > 370 :
        ball.reset_position()
        scoreboard.l_point()
    # if the ball is missed by l_player
    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.r_point()


screen.update()
screen.exitonclick()
