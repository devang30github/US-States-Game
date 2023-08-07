import turtle
import pandas


t1=turtle.Turtle()
screen=turtle.Screen()
screen.title('US State Game')
image='blank_states_img.gif'
screen.addshape(image)
t1.shape(image)


data=pandas.read_csv("50_states.csv")
states_list=data['state'].to_list()
guessed_states=[]



while len(guessed_states) < 50:
    answer_state=screen.textinput(title=f'{len(guessed_states)}/50',prompt="What's the another state's name?").title()

    if answer_state == "Exit":
        unguessed_states = [unguessed for unguessed in states_list if unguessed not in guessed_states]
        data1 = pandas.DataFrame(unguessed_states)
        data1.to_csv("unguessed_states.csv")
        break

    if answer_state in guessed_states:
        continue

    if answer_state in states_list:
        guessed_states.append(answer_state)
        t2 = turtle.Turtle()
        t2.hideturtle()
        t2.penup()
        name = data[data.state == answer_state]
        t2.goto(int(name.x),int(name.y))
        t2.write(answer_state)





