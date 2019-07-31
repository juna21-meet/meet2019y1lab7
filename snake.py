import turtle
import random 

turtle.tracer(1,0) 

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y)

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 10
TIME_STEP = 100


pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

snake = turtle.clone()
snake.shape("circle")

turtle.hideturtle()

def new_stamp():
    snake_pos = snake.pos()
   
    pos_list.append(snake_pos) 
           
    snake_stamp = snake.stamp()
        
    stamp_list.append(snake_stamp)

for i in range(START_LENGTH):
    x_pos=snake.xcor()
    y_pos=snake.ycor()

    x_pos+=SQUARE_SIZE

   

    snake.goto(x_pos,y_pos)
    new_stamp()

def remove_tail():
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp) 
    pos_list.pop(0)

snake.direction = 'Up'
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    snake.direction='Up'
   
    print("you pressed the up key!")
turtle.onkeypress(up, 'Up')


def down():
    snake.direction='Down'
    
    print("you pressed the down key!")
turtle.onkeypress(down, 'Down')


def right():
    snake.direction='Right'
    
    print("you pressed the right key!")
turtle.onkeypress(right, 'Right')


def left():
    snake.direction='Left'
    
    print("you pressed the left key!")
turtle.onkeypress(left, 'Left')
turtle.listen()
turtle.register_shape("giphy.gif")

food = turtle.clone()
food.shape("giphy.gif")

food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

for this_food_pos in food_pos :
    food.goto(this_food_pos)
    food_stamps.append(food.stamp())
    food.hideturtle()

def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

    food.goto(food_x,food_y)
    rand_food_stamp=food.stamp()
    food_pos.append((food_x,food_y))
    food_stamps.append(rand_food_stamp)


    
def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    
    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif snake.direction =="Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)   
        print("you moved down!")
    elif snake.direction == "Right":
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("you moved right!")
    elif snake.direction == "Left":
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("you moved left!")
    
    for body in pos_list:
        if snake.pos() == body:
            print("you hit yourself! GAME OVER!")
            quit()
    
    new_stamp()
    
    if snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos()) 
        food.clearstamp(food_stamps[food_index]) 
        food_pos.pop(food_index) 
        food_stamps.pop(food_index) 
        print("You have eaten the food!")
        new_stamp()
    
    
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]



    remove_tail()     
    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()
    elif new_y_pos >= UP_EDGE:
        print("You hit the top edge! Game over!")
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print("You hit the bottom edge! Game over!")
        quit()
    if len(food_stamps) <=6 :
        make_food()


    turtle.ontimer(move_snake,TIME_STEP)
    
move_snake()
    
    

turtle.mainloop()

    
