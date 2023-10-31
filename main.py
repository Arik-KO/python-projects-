from turtle import Turtle, Screen
import random

race_is_on = False
screen = Screen()
screen.setup(500, 400)
screen.bgcolor('grey')
colors = ['orange', 'blue', 'cyan', 'green', 'yellow', 'red']
user_bet = screen.textinput(title='Make Your Bet',
                            prompt='Choose a color [orange, blue, cyan, green, yellow, red] of turtle you think will win:')
all_turtle = []

if user_bet:
    race_is_on = True
for index in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-70 + (index * 40))
    all_turtle.append(new_turtle)

while race_is_on:
    for turtle in all_turtle:
        if turtle.xcor() > 220:
            winning_color = turtle.pencolor()
            race_is_on = False
            if user_bet.lower() == winning_color:
                print(f'you have won, the winning color is {winning_color}')
            else:
                print(f'you have lost, the winning color is {winning_color}')
        race_distant = random.randint(0, 8)
        turtle.forward(race_distant)

screen.exitonclick()
