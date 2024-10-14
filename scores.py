from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Italic", 25, "normal")

class ScoreBord(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.color("green")
        self.penup()
        self.goto(0,260)
        self.update()
        self.hideturtle()
        #self.game_over()
    def update(self):
        self.write(f"Score : {self.points}", align=ALIGNMENT, font=FONT)
    def increase_s(self):
        self.points+=1
        self.clear()
        self.update()
    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER...", align=ALIGNMENT, font=FONT)
