from tkinter import *
from PIL import ImageTk, Image
import numpy as np

from sprites import *
from layers import draw_character
from config import *
from ui import *

def main():
    root = Tk()  # Step 1: Create the main window
    canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()
    canvas.configure(scrollregion=canvas.bbox("all")) 
    root.resizable(width=False, height=False)
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
        'skirt': load_sprite_batch('skirt', 3),
        'blouse': load_sprite('blousetorso'),
        'tie': load_sprite_batch('tie', 3),
        'collar': load_sprite('collar'),
        'lower-sleeves': load_sprite('blousearms')
    }

    options = {'body': define_option('Body', True, 1),
               'hair': define_option('Hairstyle', True, 4),
                'eyes': define_option('Eyes', True, 3),
                'mouth': define_option('Mouth', False, 3),
                'tie': define_option('Tie', False, 3),
                'skirt': define_option('Skirt', True, 3),
                'socks': define_option('Socks', True, 3),
                'shoes': define_option('Shoes', False, 2)
                }
    
    # Save sprite data to root
    root.sprites = girl_sprites
    root.selections = {
        'body': 0,
        'hair': 0,
        'eyes': 0,
        'mouth': 0,
        'skirt': 0,
        'socks': 0,
        'shoes': 0,
    }
    root.gradient_selections = {
        'body': SKIN_GRADIENTS['Light Warm'],
        'hair': HAIR_GRADIENTS['Black'],
        'eyes': EYE_GRADIENTS['Brown'],
        'socks': SOCK_GRADIENTS['White']
    }

    # Draw background and sidebar first
    canvas.create_image(0, 0, anchor='nw', image=ui['bg'])
    canvas.create_image(0, 0, anchor='nw', image=ui['sidebar'])
    
    # Store references on root for later access
    root.canvas = canvas
    root.ui = ui
    root.options = options
    
    # Set up the main menu
    set_up(root)
    
    redraw_character(canvas, root)

    root.mainloop()  # Step 4: Start the GUI loop

'''O
Helper functions below
'''
    
if __name__ == '__main__':
    main()