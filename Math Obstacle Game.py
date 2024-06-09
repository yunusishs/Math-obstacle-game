from tkinter import *
import random

window = Tk()
window.title('Math Obstacle Game')
canvas = Canvas(window, width=800, height=600, bg = 'black')
canvas.pack()

#colour functions
def _from_rgb(rgb):
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'

def randcolour():
    return _from_rgb((random.randrange(256), random.randrange(256), random.randrange(256)))
    
def make_operators():
    global adder_text, x_position
    xposition = random.randint(0, 600)
    ender = canvas.create_rectangle(xposition, -64, xposition+64, 0, fill = randcolour())
    end_text = canvas.create_text(xposition+32, -32, text= chr(247)+ '0', font=('Cambria Math', 24, 'italic'), fill = 'black')
    enders_list.append([ender, end_text])

    xposition = random.randint(0, 600)
    if random.randrange(2) == 1:
        adder = canvas.create_rectangle(xposition, -64, xposition+64, 0, fill = randcolour())
        add_operation = random.randint(-31,31)
        if add_operation > 0:
            adder_text = canvas.create_text(xposition+32, -32, text= '+'+str(add_operation), font=('Cambria Math', 24, 'italic'), fill = 'black')
        if add_operation < 0:
            adder_text = canvas.create_text(xposition+32, -32, text= str(add_operation), font=('Cambria Math', 24, 'italic'), fill = 'black')
        if add_operation != 0:
            adders_list.append([adder, adder_text, add_operation])

    if (x > 0 and random.randrange(16) == 1) or (x < 0):
        multiplier = canvas.create_rectangle(xposition, -64, xposition+64, 0, fill = randcolour())
        multiply_operation = random.randint(0,16)
        multiplier_text = canvas.create_text(xposition+32, -32, text= chr(215)+str(multiply_operation), font=('Cambria Math', 24, 'italic'), fill = 'Black')
        multipliers_list.append([multiplier, multiplier_text, multiply_operation])

    if random.randrange(16) == 1:
        square = canvas.create_rectangle(xposition, -64, xposition+64, 0, fill = randcolour())
        square_text = canvas.create_text(xposition+32, -32, text='x'+ chr(178), font=('Cambria Math', 24, 'italic'), fill = 'black')
        squares.append([square, square_text, 'None'])

    if (x > 0 and random.randrange(8) == 1) or (x < 0):
        cube = canvas.create_rectangle(xposition, -64, xposition+64, 0, fill = randcolour())
        cube_text = canvas.create_text(xposition+32, -32, text='x'+ chr(179), font=('Cambria Math', 24, 'italic'), fill = 'black')
        cubes.append([cube, cube_text, 'None'])
    
    window.after(1000, make_operators)
    
#[0] will mean the operator square
#[1] will mean the text
#[2] will mean the operation   
def move_operators():
    for adder in adders_list:
        canvas.move(adder[0], 0, 10)
        canvas.move(adder[1], 0, 10)
        if canvas.coords(adder[0])[1] > 600:
            canvas.delete(adder[0])
            canvas.delete(adder[1])
            adders_list.remove(adder)
    for multiplier in multipliers_list:
        canvas.move(multiplier[0], 0, 10)
        canvas.move(multiplier[1], 0, 10)
        if canvas.coords(multiplier[0])[1] > 600:
            canvas.delete(multiplier[0])
            canvas.delete(multiplier[1])
            multipliers_list.remove(multiplier)
    for ender in enders_list:
        canvas.move(ender[0], 0, 10)
        canvas.move(ender[1], 0, 10)
        enderx=canvas.coords(ender[0])[0]
        endery=canvas.coords(ender[0])[1]
        xx=canvas.coords(player)[0]
        xy=canvas.coords(player)[1]
        if enderx > xx:
            canvas.move(ender[0], -1,0)
            canvas.move(ender[1], -1,0)
        if enderx < xx:
            canvas.move(ender[0], 1, 0)
            canvas.move(ender[1], 1, 0)
        if endery > xy:
            canvas.move(ender[0], 0,-1)
            canvas.move(ender[1], 0,-1)
        if endery < xy:
            canvas.move(ender[0], 0, 1)
            canvas.move(ender[1], 0, 1)
        if canvas.coords(ender[0])[1] > 600:
            canvas.delete(ender[0])
            canvas.delete(ender[1])
            enders_list.remove(ender)
    for square in squares:
        canvas.move(square[0], 0, 10)
        canvas.move(square[1], 0, 10)
        if canvas.coords(square[0])[1] > 600:
            canvas.delete(square[0])
            canvas.delete(square[1])
            squares.remove(square)
    for cube in cubes:
        canvas.move(cube[0], 0, 10)
        canvas.move(cube[1], 0, 10)
        if canvas.coords(cube[0])[1] > 600:
            canvas.delete(cube[0])
            canvas.delete(cube[1])
            cubes.remove(cube)
    window.after(50, move_operators)

def collision(item1, item2, distance):
    xdistance = abs(canvas.coords(item1)[0] - canvas.coords(item2)[0])
    ydistance = abs(canvas.coords(item1)[1] - canvas.coords(item2)[1])
    overlap = xdistance < distance and ydistance < distance
    return overlap

def check_hits():
    global x
    for adder in adders_list:
        if collision(player, adder[0], 64):
            x = x + adder[2]
            canvas.delete(adder[0])
            canvas.delete(adder[1])
            adders_list.remove(adder)
            
    for multiplier in multipliers_list:
        if collision(player, multiplier[0], 64):
            x = x*multiplier[2]
            canvas.delete(multiplier[0])
            canvas.delete(multiplier[1])
            multipliers_list.remove(multiplier)
            
    for ender in enders_list:
        if collision(player, ender[0], 64):
            canvas.create_text(400,300, text='Game Over', font=('Cambria math', 32, 'italic'), fill='red')
            x = x/0
            canvas.delete(ender[0])
            canvas.delete(ender[1])
            enders_list.remove(ender)

    for square in squares:
        if collision(player, square[0], 64):
            x = x*x
            canvas.delete(square[0])
            canvas.delete(square[1])
            squares.remove(square)

    for cube in cubes:
        if collision(player, cube[0], 64):
            x = x**3
            canvas.delete(cube[0])
            canvas.delete(cube[1])
            cubes.remove(cube)
    x_display.configure(text="x=" + str(x))
    window.after(100, check_hits)

def check_input(event):
    global move_direction
    key = event.keysym
    if key == "Right" or key.lower() == "d":
        move_direction = "Right"
    elif key == "Left" or key.lower() == "a":
        move_direction = "Left"
    elif key == "Up" or key.lower() == "w":
        move_direction = "Up"
    elif key == "Down" or key.lower() == "s":
        move_direction = "Down"
        
def end_input(event):
    global move_direction
    move_direction = "None"
    
def move_player():
    if move_direction == "Right" and canvas.coords(player)[0] < 800 and canvas.coords(player_text)[0] < 800:
        canvas.move(player, 10,0)
        canvas.move(player_text, 10,0)
    elif move_direction == "Left" and canvas.coords(player)[0] > 0 and canvas.coords(player_text)[0] > 0:
        canvas.move(player, -10,0)
        canvas.move(player_text, -10,0)
    elif move_direction == "Up" and canvas.coords(player)[1] > 0 and canvas.coords(player_text)[1] > 0:
        canvas.move(player, 0,-10)
        canvas.move(player_text, 0,-10)
    elif move_direction == "Down" and canvas.coords(player)[1] < 600 and canvas.coords(player_text)[1] < 600:
        canvas.move(player, 0,10)
        canvas.move(player_text, 0,10)
    window.after(16, move_player)

#setup player x   
x = 0
x_display = Label(window, text="x=" + str(x), font=('Cambria Math', 16, 'italic'))
x_display.pack()

player = canvas.create_rectangle(368,268,432,332, fill='blue')
player_text = canvas.create_text(400,300, text='x', font=('Cambria Math', 32, 'italic'), fill='white')

#make lists
adders_list = [] 
multipliers_list = []
enders_list = []
squares = []

#setup movement
cubes = []

move_direction = 0

canvas.bind_all('<KeyPress>', check_input) 
canvas.bind_all('<KeyRelease>', end_input)

#run functions
window.after(1000, make_operators)
window.after(1000, move_operators)
window.after(1000, check_hits)
window.after(1000, move_player)

window.mainloop()
