import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. State Game")

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
allStates = df.state.to_list()
guessedStates = []


while len(guessedStates) < 50:
    answerState = screen.textinput(title=f"{len(guessedStates)}/50 States guessed", prompt="What's the another state "
                                                                                           "name?").title()
    if answerState == "Exit":
        missingStates = []
        for state in allStates:
            if state not in guessedStates:
                missingStates.append(state)
        newData = pd.DataFrame(missingStates)
        newData.to_csv("StatestoLearn.csv")
        break

    if answerState in allStates:
        guessedStates.append(answerState)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answerState]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answerState)
