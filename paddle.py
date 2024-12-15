from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("square")
        self.shapesize(stretch_wid= 5, stretch_len= 1)
        self.penup()


    def go_up(self):
        y = self.ycor() + 50
        self.goto(self.xcor(), y)

    def go_down(self):
        y = self.ycor() - 50
        self.goto(self.xcor(), y)
