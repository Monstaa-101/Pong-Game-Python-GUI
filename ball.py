from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        x_cord = self.xcor() + self.x_move
        y_cord = self.ycor() + self.y_move
        self.goto(x_cord, y_cord)

    def bounce(self):
        self.y_move = -self.y_move

    def hit(self):
        self.x_move = -self.x_move
        self.move_speed *= 0.5

    def fast(self):
        self.x_move*10
        self.y_move*10

    def r_reset_position(self):
        self.move_speed = 0.1
        self.goto(0,0)
        self.x_move = -self.x_move

    def l_reset_position(self):
        self.move_speed = 0.1
        self.goto(0,0)
        self.x_move = -self.x_move
