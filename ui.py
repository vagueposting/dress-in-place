from tkinter import *
from PIL import ImageTk, Image
from sprites import load_sprite
from config import *

def set_up(root, canvas, ui, options):
    # Creates a setup.
    # remember: left_x, top_y, right_x, bottom_y

    # Draw the sidebar
    canvas.create_image(0, 0,
                    anchor='nw',
                    image=ui['bg'])

    canvas.create_image(0, 0,
                    anchor='nw',
                    image=ui['sidebar'])
    
    draw_menu(root, options, starting_x = SIDEBAR_MAX // 5,
              starting_y = CANVAS_HEIGHT // 6, width_px = 70,
              height_px = 60, gap_x = 90, gap_y = 70)

def load_ui(sprite_name):
    return ImageTk.PhotoImage(load_sprite(sprite_name))

def draw_button(parent, text, x, y, width_px=70, height_px=60):
    btn = Button(
        parent,
        text=text,
        font=("Arial", 10),
        padx=width_px // 10,   # Rough estimate
        pady=height_px // 10,
        fg='black',
        bd=2,
        relief='solid',
        highlightthickness=2,
        highlightbackground='black',
        highlightcolor='black',
        borderwidth=2
    )
    btn.place(x=x, y=y)
    return btn

def draw_menu(parent, options, starting_x, 
              starting_y, width_px, height_px, 
              gap_x, gap_y):
    x = starting_x
    y = starting_y
    button_count = 0

    for key in options:
        draw_button(parent,
                    options[key]['name'], 
                    x, 
                    y, 
                    width_px, 
                    height_px)
        # Button positioning
        if button_count % 2 == 0:
            x += gap_x
        else:
            y += gap_y
            x = starting_x
        
        button_count += 1 

        