from tkinter import *
from PIL import ImageTk, Image
from sprites import load_sprite
from config import *

def set_up(root, canvas, ui):
    # Creates a setup.
    # remember: left_x, top_y, right_x, bottom_y

    # Draw the sidebar
    canvas.create_image(0, 0,
                    anchor='nw',
                    image=ui['bg'])

    canvas.create_image(0, 0,
                    anchor='nw',
                    image=ui['sidebar'])

    draw_button(root, "Hair",
            x=SIDEBAR_MAX // 3,
            y=CANVAS_HEIGHT // 5)

def load_ui(sprite_name):
    return ImageTk.PhotoImage(load_sprite(sprite_name))

def draw_button(parent, text, x, y, width_px=70, height_px=60):
    btn = Button(
        parent,
        text=text,
        font=("Arial", 10),
        padx=width_px // 10,   # Rough estimate
        pady=height_px // 10,
        bg='white',
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