from tkinter import *
from PIL import ImageTk, Image
import numpy as np

from sprites import load_sprite, load_sprite_batch
from layers import draw_character
from config import CANVAS_WIDTH, CANVAS_HEIGHT, LAYER_ORDER, CHARACTER_POS_X, CHARACTER_POS_Y

def main():
    root = Tk()  # Step 1: Create the main window
    canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()
    canvas.tk_images = [] 

    set_up(canvas)

    # Define gradients

    # Load sprites
    # For multiple pieces, use load_sprite_batch()
    sprites = {
        # Body parts: head, torso-and-legs, lower-arms-hair, eyes, mouth
        'head': load_sprite('head'),
        'torso-and-legs': load_sprite('torso-and-legs'),
        'lower-arms': load_sprite('lower-arms'),
        'hair': load_sprite_batch('hair', 4),
        'eyes': load_sprite_batch('eye', 3),
        'mouth': load_sprite_batch('mouth', 3),
        # Clothing: shoes, socks, skirt, blouse, tie, collar, lower sleeves
        'socks': load_sprite_batch('socks', 3),   
        'shoes': load_sprite_batch('shoes', 2),
        'skirt': load_sprite_batch('skirt', 2),
        'blouse': load_sprite('blousetorso'),
        'tie': load_sprite_batch('tie', 3),
        'collar': load_sprite('collar'),
        'lower-sleeves': load_sprite('blousearms')
    }

    test_selections = {
        'hair': 3,
        'eyes': 0,
        'mouth': 0,
        'skirt': 1,
        'socks': 1,
        'shoes': 0,
    }

    draw_character(canvas, sprites, CHARACTER_POS_X, CHARACTER_POS_Y, test_selections)

    """
    TEST CODE BELOW!!
    # Load your grayscale sprite (must be black/white line art)
    head = Image.open("img/small/head.png").convert('RGBA')
    hair = Image.open("img/small/hair1.png").convert('RGBA')

    # Define a gradient using hex codes
    gradient_colors = ["#872222", "#834611", "#ffe5be"]  # Red → Pink → White

    # Create gradient map
    gradient = create_gradient_map(gradient_colors, size=(256, 1))

    # Apply gradient to sprite
    recolored_head = apply_gradient(head, gradient)

    # Convert to Tkinter-compatible image
    tk_sprite = ImageTk.PhotoImage(recolored_head)
    tk_hair = ImageTk.PhotoImage(hair)

    # Draw on canvas
    canvas.create_image(CHARACTER_POS_X, CHARACTER_POS_Y, image=tk_sprite)
    canvas.create_image(CHARACTER_POS_X, CHARACTER_POS_Y, anchor='center', image=tk_hair)
    canvas.tk_sprite = tk_sprite  # Keep reference!
    """

    root.mainloop()  # Step 4: Start the GUI loop

"""
Helper functions below
"""

def set_up(canvas):
    # Creates a setup.
    # remember: left_x, top_y, right_x, bottom_y

    # Draw the sidebar
    # TODO: Replace with actual graphics.
    canvas.create_rectangle(0,
                            0, 
                            CANVAS_WIDTH / 3, 
                            CANVAS_HEIGHT, 
                            fill='aquamarine')
    
    center_x = CANVAS_WIDTH / 6  # Half of the sidebar width (since sidebar is CANVAS_WIDTH/3)
    center_y = CANVAS_HEIGHT / 10  # Same vertical position

    canvas.create_text(
        center_x,
        center_y,
        anchor='center',
        justify='center',
        font=('Arial', 11),
        text="Welcome!\nI'm getting ready for school,\nand I really need your help!"
    )
    
if __name__ == '__main__':
    main()