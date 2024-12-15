from turtle import Turtle


class CentreLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color("orange")
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.pendown()
        self.width(5)
        self.setheading(270)
        while self.ycor() >= -300:
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
