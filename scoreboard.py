from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.font_settings = ("Arial", 23, "bold")
        self.l_score = 0
        self.r_score = 0

    def ratio_diff(self,x,y):
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.color("gray")
        self.pendown()
        self.write(":",font=self.font_settings, align="center")

    def show_score(self,x,y):
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.color("gray")
        self.pendown()
        self.write(self.score, font=self.font_settings, align="center")

    def plus_point(self):
        self.score += 1