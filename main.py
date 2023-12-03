import turtle
screen = turtle.Screen()
pen = turtle.Turtle()
def draw_square():
    for _ in range(4):
        pen.forward(100)
        pen.right(90)
draw_square()
