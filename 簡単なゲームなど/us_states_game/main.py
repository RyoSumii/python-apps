import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic(image)

turtle.addshape(image)
turtle.penup()
turtle.ht()

data = pd.read_csv("50_states.csv")
answer_list = []
score = len(answer_list)

game_is_on = True
while score < 50:

    if score == 0:
        answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    else:
        answer_state = screen.textinput(title=f"{score}/50 Guess the State", prompt="What's another state's name?")

    answer_state = answer_state.title()
    if answer_state == "Exit":

        break

    if answer_state in answer_list:
        continue

    if answer_state in data.state.values:
        score += 1
        answer_list.append(answer_state)
        x_data = data.x[data.state == answer_state].values[0]
        y_data = data.y[data.state == answer_state].values[0]
        turtle.goto(x_data, y_data)
        turtle.write(arg=answer_state, align="center", font=("Arial", 8, "normal"))


list_data = data.state.to_list()

for state in list_data:
    if state in answer_list:
        list_data.remove(state)
list_data = pd.Series(list_data)
list_data.to_csv("missing_states", header=False, index=False)
