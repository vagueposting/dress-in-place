from tkinter import *
from PIL import ImageTk, Image
import numpy as np

from sprites import load_sprite, load_sprite_batch
from layers import draw_character
from config import *
from ui import *

def main():
    root = Tk()  # Step 1: Create the main window
    canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()
    canvas.tk_images = [] 

    # Define gradients

    # Load sprites
    # For multiple pieces, use load_sprite_batch()
    ui = {
        'bg': load_ui('bg_root'),
        'sidebar': load_ui('ui_sidebar'),
        'speech-bubble': load_ui('ui_speech-bubble')
    }
    girl_sprites = {
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
    # TODO: Make this into a dictionary of dictionaries.
    options = {'recolorable': ('hair', 'mouth',
                               'skirt', 'socks'),
                'non-recolorable': ('mouth')}

    test_selections = {
        'hair': 3,
        'eyes': 0,
        'mouth': 0,
        'skirt': 1,
        'socks': 1,
        'shoes': 0,
    }

    set_up(root, canvas, ui)
    draw_character(canvas, girl_sprites, CHARACTER_POS_X, CHARACTER_POS_Y, test_selections)

    """
    TEST CODE BELOW!!
    TODO: Write the actual code, then remove!
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

"""O
Helper functions below
"""
    
if __name__ == '__main__':
    main()