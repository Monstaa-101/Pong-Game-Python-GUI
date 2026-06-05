from turtle import Turtle

class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.pensize(15)
        self.font_settings = ("Arial", 30, "bold")

    def upBound(self):
        self.penup()
        self.goto(-420, 290)
        self.pendown()
        self.right(90)
        self.goto(420, 290)
        self.penup()
        self.hideturtle()

    def downBound(self):
        self.penup()
        self.goto(-420, -285)
        self.pendown()
        self.right(90)
        self.goto(420, -285)
        self.penup()
        self.hideturtle()

    def rightBound(self):
        self.penup()
        self.color("navy")
        self.goto(390, 270)
        self.pendown()
        self.right(90)
        self.goto(390, -270)
        self.penup()
        self.hideturtle()

    def leftBound(self):
        self.penup()
        self.color("navy")
        self.goto(-398, 270)
        self.pendown()
        self.right(90)
        self.goto(-398, -270)
        self.penup()
        self.hideturtle()

    def title(self,name,x,y):
        self.penup()
        self.color("gold")
        self.goto(x,y)
        self.pendown()
        self.write(name, font=self.font_settings, align="center")
        self.hideturtle()

    def gameOver(self,name,x,y):
        self.penup()
        self.color("Blue")
        self.goto(x,y)
        self.pendown()
        self.write(name, font=self.font_settings, align="center")
        self.hideturtle()