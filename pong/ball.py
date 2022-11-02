from turtle import Turtle
from time import sleep

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(0,0)
        self.x_dir = 10
        self.y_dir = 10
    
    def move(self):
        sleep(.04)
        self.goto(self.xcor()+self.x_dir,self.ycor()+self.y_dir)
  
    def bounce_y(self):
        self.y_dir *= -1

    def bounce_x(self):
        self.x_dir *= -1
    
    def reset_position(self):
        self.goto(0,0)
        
  

        
    