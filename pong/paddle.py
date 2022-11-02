from turtle import Turtle, setheading, shape
up = 90

class Paddle(Turtle,):
    def __init__(self,side = ""):
        super().__init__()
        if side == "right":
            self.goto(280,0)
        else:
            self.goto(-280,0)
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(5,1)
    
    def up(self):
        if not self.ycor() > 200: 
            self.goto(self.xcor(),self.ycor()+20)
    
    def down(self):
        if not self.ycor() < -200:
            self.goto(self.xcor(),self.ycor()-20)
       
            


        
            


                    


        
