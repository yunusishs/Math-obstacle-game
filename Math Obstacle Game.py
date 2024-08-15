from tkinter import *
import random

#colour functions
def _from_rgb(rgb):
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'

def randcolour():
    red = random.randrange(256)
    green = random.randrange(256)
    blue = random.randrange(256)
    return [_from_rgb((red, green, blue)), _from_rgb((255-red, 255-green, 255-blue))]

#making the operators

def operator_configs():
    global xposition, yposition, colour
    xposition = random.randint(64, canvas_width)
    yposition = random.randint(-1024, 0)
    colour = randcolour()

''' 
[0] will mean the operator square
[1] will mean the text
[2] will mean the operation
'''

def make_operators():
    operator_configs()
    zero_division = canvas.create_rectangle(xposition, yposition, xposition-64, yposition-64, fill = colour[0])
    zero_division_text = canvas.create_text(xposition-32, yposition-32, text= chr(247)+ '0', font=('Cambria Math', 20, 'italic'), fill = colour[1])
    zero_division_list.append([zero_division, zero_division_text])

    operator_configs()
    adder = canvas.create_rectangle(xposition, yposition, xposition-64, yposition-64, fill = colour[0])
    add_operation = 0
    while add_operation == 0:
        add_operation = random.randint(-32,32)
    if add_operation > 0:
        display = '+'+str(add_operation)
    if add_operation < 0:
        display = str(add_operation)
    adder_text = canvas.create_text(xposition-32, yposition-32, text= display, font=('Cambria Math', 20, 'italic'), fill = colour[1])
    adders_list.append([adder, adder_text, add_operation])

    operator_configs()
    if (x > 0 and random.randrange(4) == 1) or (x < 0):
        multiplier = canvas.create_rectangle(xposition, yposition, xposition-64, yposition-64, fill = colour[0])
        multiply_operation = 1
        while multiply_operation == 1:
            multiply_operation = random.randint(-1,10)
        if multiply_operation == -1:
            if random.randrange(2) == 1:
                display = chr(247)+str(multiply_operation)
            else:
                display = chr(215)+str(multiply_operation)
        else:
            display = chr(215)+str(multiply_operation)

        multiplier_text = canvas.create_text(xposition-32, yposition-32, text = display, font=('Cambria Math', 20, 'italic'), fill = colour[1])
        multipliers_list.append([multiplier, multiplier_text, multiply_operation])
        
    operator_configs()
    if random.randrange(16) == 1:
        square = canvas.create_rectangle(xposition, yposition, xposition-64, yposition-64, fill = colour[0])
        square_text = canvas.create_text(xposition-32, yposition-32, text='x'+ chr(178), font=('Cambria Math', 20, 'italic'), fill = colour[1])
        squares_list.append([square, square_text])
        
    operator_configs()
    if (x > 0 and random.randrange(16) == 1) or (x < 0):
        cube = canvas.create_rectangle(xposition, yposition, xposition-64, yposition-64, fill = colour[0])
        cube_text = canvas.create_text(xposition-32, yposition-32, text='x'+ chr(179), font=('Cambria Math', 20, 'italic'), fill = colour[1])
        cubes_list.append([cube, cube_text])
    
    window.after(1024, make_operators)
        
def move_operators():
    for operator_list in lists:
        if operator_list == zero_division_list:
            pass
        for operator in operator_list:
            canvas.move(operator[0], 0, 4)
            canvas.move(operator[1], 0, 4)
            if canvas.coords(operator[0])[1] > canvas_height:
                canvas.delete(operator[0])
                canvas.delete(operator[1])
                operator_list.remove(operator)
    window.after(16, move_operators)

def collision(item1, item2, distance):
    xdistance = abs(canvas.coords(item1)[0] - canvas.coords(item2)[0])
    ydistance = abs(canvas.coords(item1)[1] - canvas.coords(item2)[1])
    overlap = xdistance < distance and ydistance < distance
    return overlap
            
def check_hits():
    global x
    for operator_list in lists:
        for operator in operator_list:
            if collision(player, operator[0], 64):
                if operator_list == adders_list:
                    x = x + operator[2]
                if operator_list == multipliers_list:
                    x = x * operator[2]
                if operator_list == zero_division_list:
                    canvas.create_text(canvas.coords(player_text)[0], canvas.coords(player_text)[1], text='Game Over', font=('Cambria math', 32, 'italic'), fill='red')
                    x = x/0
                if operator_list == squares_list:
                    x = x*x
                if operator_list == cubes_list:
                    x = x**3
                canvas.delete(operator[0])
                canvas.delete(operator[1])
                operator_list.remove(operator)
    x_display.configure(text="x=" + str(x))
    window.after(1, check_hits)

def check_input(event):
    global move_direction, game_started
    key = event.keysym
    if key == "Right" or key.lower() == "d":
        move_direction = "Right"
    elif key == "Left" or key.lower() == "a":
        move_direction = "Left"
    elif key == "Up" or key.lower() == "w":
        move_direction = "Up"
    elif key == "Down" or key.lower() == "s":
        move_direction = "Down"
    elif key == "space":
        game_started = True
        
def end_input(event):
    global move_direction
    move_direction = "None"
    
def move_player():
    if move_direction == "Right" and canvas.coords(player)[0] < canvas_width and canvas.coords(player_text)[0] < canvas_width:
        canvas.move(player, 10,0)
        canvas.move(player_text, 10,0)
    elif move_direction == "Left" and canvas.coords(player)[0] > 0 and canvas.coords(player_text)[0] > 0:
        canvas.move(player, -10,0)
        canvas.move(player_text, -10,0)
    elif move_direction == "Up" and canvas.coords(player)[1] > 0 and canvas.coords(player_text)[1] > 0:
        canvas.move(player, 0,-10)
        canvas.move(player_text, 0,-10)
    elif move_direction == "Down" and canvas.coords(player)[1] < canvas_height and canvas.coords(player_text)[1] < canvas_height:
        canvas.move(player, 0,10)
        canvas.move(player_text, 0,10)
    window.after(16, move_player)

def start_game():
    if not game_started:
        window.after(1, start_game)
    if game_started:
        canvas.delete(title)
        canvas.delete(directions)
        canvas.delete(press_to_start)
        make_operators()
        move_operators()
        check_hits()
        move_player()
        
#set up window and canvas
window = Tk()
window.title('Math Obstacle Game')
canvas_width = 1280
canvas_height = 640
canvas = Canvas(window, width=canvas_width, height=canvas_height, bg = 'black')
canvas.pack()

#setup player x   
x = 0
x_display = Label(window, text="x=" + str(x), font=('Cambria Math', 16, 'italic'))
x_display.pack()

player = canvas.create_rectangle(canvas_width/2-32, canvas_height/2+128, canvas_width/2+32, canvas_height/2+192, fill='blue')
player_text = canvas.create_text(canvas_width/2,canvas_height/2+160, text='x', font=('Cambria Math', 32, 'italic'), fill='white')

title = canvas.create_text(canvas_width/2, canvas_height/2-64, text= 'Math Obstacle Game', fill='white', font = ('consolas', 32,'bold'))
directions = canvas.create_text(canvas_width/2, canvas_height/2, text= 'Get the highest score possible', fill='white', font = ('consolas', 24))
press_to_start = canvas.create_text(canvas_width/2, canvas_height/2+64, text="Press 'space' to start", fill='white', font = ('consolas',16))

#make lists
adders_list = [] 
multipliers_list = []
zero_division_list = []
squares_list = []
cubes_list = []
lists = [adders_list, multipliers_list, zero_division_list, squares_list, cubes_list]

#setup movement
move_direction = 0

canvas.bind_all('<KeyPress>', check_input) 
canvas.bind_all('<KeyRelease>', end_input)

game_started = False

#run functions
start_game()

window.mainloop()
