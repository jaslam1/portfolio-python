from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        
        self.penup()
        
        self.color("green")
        
        self.goto(STARTING_POSITION)
        
        self.shape("turtle")
        
        self.left(90)
    
    def move_up(self):
        self.goto(self.xcor(),self.ycor()+MOVE_DISTANCE)
        
        if self.ycor() > FINISH_LINE_Y:
            
            self.goto(STARTING_POSITION)

    def move_down(self):
        if self.ycor() == -280:
            pass 
        else:
            self.goto(self.xcor(),self.ycor()-MOVE_DISTANCE)


