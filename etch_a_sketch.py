from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()


def tim_forward():
    tim.forward(10)


def tim_backward():
    tim.backward(10)


def tim_clock():
    tim.left(5)


def tim_anti():
    tim.right(5)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key='d', fun=tim_forward)
screen.onkey(key='a', fun=tim_backward)
screen.onkey(key='w', fun=tim_clock)
screen.onkey(key='s', fun=tim_anti)
screen.onkey(key='c', fun=clear)

screen.exitonclick()
