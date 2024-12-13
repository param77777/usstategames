import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = r"C:\Users\tyt36\OneDrive\Desktop\All\GitDemo\usstatequiz\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# To get the x,y coordinates and store them in csv file
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv(r"C:\Users\tyt36\OneDrive\Desktop\All\GitDemo\usstatequiz\50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="What's another state's name?").title()
    print(answer_state)
    
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
                new_data = pandas.DataFrame(missing_states)
                new_data.to_csv("states_to_learn.csv")
        break
    
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()  # Add parentheses to create a new turtle object
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state) 
        
