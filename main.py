from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
width = 500
length = 400
Xmargin = 10
Ymargin = 30
distance_between_turtles = 30


def init_turtles():
    turtles = []

    for i in range(0, len(colors)):
        t = Turtle(shape='turtle', visible=True)
        t.color(colors[i])
        t.penup()
        t.goto(-(width / 2) + Xmargin, -(length / 4) + Ymargin + distance_between_turtles * i)
        turtles.append(t)
    return turtles


def main():
    scr = Screen()
    scr.setup(width, length)
    user_bet = scr.textinput(title="Place your bet", prompt="Which color is gonna win the race?")
    turtle_list = init_turtles()
    win_t = run_loop(turtle_list)
    if check_bet(win_t, user_bet):
        print("You have won the bet!")
    else:
        print(f"You have lost the bet! The {win_t.color()[0]} turtle won the race")
    scr.exitonclick()


def run_loop(turtles):
    win_t = None
    has_winner = False
    while not has_winner:
        move(turtles)
        win_t = check_for_winner(turtles)
        if win_t is not None:
            has_winner = True
    return win_t


def check_bet(t, user_bet):
    return t.color()[0] == user_bet


def get_random_move(limit):
    return random.randint(0, limit)


def check_for_winner(turtles):
    for t in turtles:
        if t.xcor() >= (width / 2) - Xmargin:
            return t
    return None


def move(turtles):
    for t in turtles:
        t.forward(get_random_move(10))


main()
