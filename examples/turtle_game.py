from turtle import *
from random import randint

def set_race():
    """Start from top left"""
    setup(420, 420, 370, 0)
    speed(0)
    penup()
    goto(-140, 140)

    """Draw finish line"""
    for step in range(15):
        write(step, align="center")
        right(90)
        forward(10)
        pendown()
        forward(150)
        penup()
        backward(160)
        left(90)
        forward(20)

    """Create the racers"""
    george = Turtle(shape="turtle")
    george.color("green"); george.penup(); george.goto(-160, 100)

    julia = Turtle(shape="turtle")
    julia.color("red"); julia.penup(); julia.goto(-160, 70)

    """Start the race"""
    for turn in range(100):
        george.forward(randint(1, 5))
        julia.forward(randint(1, 5))

set_race()
done()