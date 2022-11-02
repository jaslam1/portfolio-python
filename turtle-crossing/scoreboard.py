from turtle import Turtle, update


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(-210,260)
        self.write(f"level : {self.score}",0,"center",FONT)
        self.penup()
        self.hideturtle()
        self.update()
        self.goto(-210,260)
    
    def scored(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"level : {self.score}",0,"center",FONT)
    
