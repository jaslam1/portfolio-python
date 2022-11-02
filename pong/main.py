from turtle import Screen, listen, onkey, onkeypress
import turtle
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard




screen = Screen()
screen.bgcolor("black")
screen.screensize(600,500)
screen.tracer(0)


left_paddle = Paddle("left")
right_paddle = Paddle("right")
onkeypress(right_paddle.up,"Up")  
onkeypress(right_paddle.down,"Down")
onkeypress(left_paddle.up,"w")  
onkeypress(left_paddle.down,"s")

scoreboard = Scoreboard() 
ball = Ball() 
listen()
game_end = False
while game_end == False:
    screen.update()
    ball.move()
    if ball.ycor() > 250 or ball.ycor() < -250:
        ball.bounce_y()

    if ball.distance(right_paddle) < 60 and ball.xcor() > 260 and ball.xcor() <= 270 or  ball.distance(left_paddle) < 60 and ball.xcor() < -260 and ball.xcor() <= -270:
        ball.bounce_x()

    if ball.xcor() > 300:
        scoreboard.l_point()
        ball.reset_position()
         
    elif ball.xcor() < -300:
        scoreboard.r_point()
        ball.reset_position()
        
    
   
        





screen.exitonclick()