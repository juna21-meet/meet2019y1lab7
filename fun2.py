'''
import turtle
turtle.goto(0,0)

def up():
    print('you pressed the up key.')

turtle.onkey(up, "Up")
turtle.goto(0,0)
turtle.listen()
turtle.mainloop()
'''


import turtle
turtle.goto(0,0)

turtle.direction = None

def up():
    turtle.direction = "Up"
    print("you pressed the up key.")
    on_move()
    
def down():
    turtle.direction = "Down"
    print("you pressed the down key")
    on_move()


def right():
    turtle.direction = "Right"
    print("you pressed the right key")
    on_move()


def left():
    turtle.direction = "Left"
    print("you pressed the left key")
    on_move()

turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(right, "Right")
turtle.onkey(left, "Left")

turtle.listen()


def on_move():
    x,y = turtle.pos()
    if turtle.direction == "Up":
        turtle.goto(x,y+100)
    elif turtle.direction == "Down":
        turtle.goto(x,y-100)
    elif turtle.direction == "Right":
        turtle.goto(x+100,y)
    elif turtle.direction == "Left":
        turtle.goto(x-100,y)
    else:
        print("done")

        
turtle.mainloop()
    

 


    

