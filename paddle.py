from turtle import Turtle

line = Turtle()


def center_line():
    line.color('white')
    line.hideturtle()
    line.penup()
    line.goto(0, -400)
    line.setheading(90)
    for lane in range(0, 20):
        line.pendown()
        line.forward(20)
        line.penup()
        line.forward(20)


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.goto(position)

    def go_up(self):
        if self.ycor() <= 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() >= -220:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

