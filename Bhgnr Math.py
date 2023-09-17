from tkinter import *
import random

window = Tk()
window.title('Bhgnr Math')
canvas = Canvas(window, width=800, height=600, bg = 'black')
canvas.pack()

x = 0
x_display = Label(window, text="x=" + str(x), font=('Cambria Math', 16, 'italic'))
x_display.pack()

mychar = canvas.create_rectangle(368,268,432,332, fill='blue')
mychar_text = canvas.create_text(400,300, text='x', font=('Cambria Math', 32, 'italic'), fill='white')

adders_list = [] 
multipliers_list = []
enders_list = []
squares = []
cubes = []

adder_text = ''
x_position=0
    
def make_operators():
    global adder_text, x_position
    xposition = random.randint(0, 600)
    addition_color=random.choice(['light green', 'green', 'dark green'])
    multiplcation_color=random.choice(['cyan', 'light blue', 'blue', 'dark blue'])
    power_color=random.choice(['grey', 'black'])
    if random.randint(0,4) == 1:
        adder = canvas.create_rectangle(xposition, -64, xposition+64, 0, fill = addition_color)
        add_operation = random.randint(-31,16)
        if add_operation > 0:
            adder_text = canvas.create_text(xposition+32, -32, text= '+'+str(add_operation), font=('Cambria Math', 24, 'italic'), fill = 'Black')
        if add_operation < 0:
            adder_text = canvas.create_text(xposition+32, -32, text= str(add_operation), font=('Cambria Math', 24, 'italic'), fill = 'black')
        if add_operation != 0:
            adders_list.append([adder, adder_text, add_operation])

    if (x < 0 and random.randint(0,16) == 1) or (x < 0):
        xposition = random.randint(0, 600)
        multiplier = canvas.create_rectangle(xposition, -64, xposition+64, 0, fill = multiplcation_color)
        multiply_operation = random.randint(0,16)
        multiplier_text = canvas.create_text(xposition+32, -32, text= chr(215)+str(multiply_operation), font=('Cambria Math', 24, 'italic'), fill = 'Black')
        multipliers_list.append([multiplier, multiplier_text, multiply_operation])

    if 1 == 1:
        xposition = random.randint(0, 600)
        ender = canvas.create_rectangle(xposition, -64, xposition+64, 0, fill = multiplcation_color)
        end_text = canvas.create_text(xposition+32, -32, text= chr(247)+ '0', font=('Cambria Math', 24, 'italic'), fill = 'Black')
        enders_list.append([ender, end_text])

    if random.randint(1,32) == 1:
        xposition = random.randint(0, 600)
        square = canvas.create_rectangle(xposition, -64, xposition+64, 0, fill = power_color)
        square_text = canvas.create_text(xposition+32, -32, text='x'+ chr(178), font=('Cambria Math', 24, 'italic'), fill = 'white')
        squares.append([square, square_text, 'None'])

    if (x < 0 and random.randint(0,8) == 1) or (x < 0):
        xposition = random.randint(0, 600)
        cube = canvas.create_rectangle(xposition, -64, xposition+64, 0, fill = power_color)
        cube_text = canvas.create_text(xposition+32, -32, text='x'+ chr(179), font=('Cambria Math', 24, 'italic'), fill = 'white')
        cubes.append([cube, cube_text, 'None'])
    
    window.after(1000, make_operators)
    
#[0] will mean the operator itself
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
        xx=canvas.coords(mychar)[0]
        xy=canvas.coords(mychar)[1]
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
        if collision(mychar, adder[0], 64):
            x = x + adder[2]
            canvas.delete(adder[0])
            canvas.delete(adder[1])
            adders_list.remove(adder)
            
    for multiplier in multipliers_list:
        if collision(mychar, multiplier[0], 64):
            x = x*multiplier[2]
            canvas.delete(multiplier[0])
            canvas.delete(multiplier[1])
            multipliers_list.remove(multiplier)
            
    for ender in enders_list:
        if collision(mychar, ender[0], 64):
            canvas.create_text(400,300, text='Game Over', font=('Cambria math', 32, 'italic'), fill='red')
            x = x/0
            canvas.delete(ender[0])
            canvas.delete(ender[1])
            enders_list.remove(ender)

    for square in squares:
        if collision(mychar, square[0], 64):
            x = x*x
            canvas.delete(square[0])
            canvas.delete(square[1])
            squares.remove(square)

    for cube in cubes:
        if collision(mychar, cube[0], 64):
            x = x*x*x
            canvas.delete(cube[0])
            canvas.delete(cube[1])
            cubes.remove(cube)
    x_display.configure(text="x=" + str(x))
    window.after(100, check_hits)

move_direction = 0
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
    
def move_character():
    if move_direction == "Right" and canvas.coords(mychar)[0] < 800 and canvas.coords(mychar_text)[0] < 800:
        canvas.move(mychar, 10,0)
        canvas.move(mychar_text, 10,0)
    elif move_direction == "Left" and canvas.coords(mychar)[0] > 0 and canvas.coords(mychar_text)[0] > 0:
        canvas.move(mychar, -10,0)
        canvas.move(mychar_text, -10,0)
    elif move_direction == "Up" and canvas.coords(mychar)[1] > 0 and canvas.coords(mychar_text)[1] > 0:
        canvas.move(mychar, 0,-10)
        canvas.move(mychar_text, 0,-10)
    elif move_direction == "Down" and canvas.coords(mychar)[1] < 600 and canvas.coords(mychar_text)[1] < 600:
        canvas.move(mychar, 0,10)
        canvas.move(mychar_text, 0,10)
    window.after(16, move_character)

canvas.bind_all('<KeyPress>', check_input) 
canvas.bind_all('<KeyRelease>', end_input)


window.after(1000, make_operators)
window.after(1000, move_operators)

window.after(1000, check_hits)

window.after(1000, move_character)

window.mainloop()

