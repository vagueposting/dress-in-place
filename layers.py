from tkinter import *
from PIL import ImageTk, Image
from config import LAYER_ORDER

def draw_character(canvas, sprites, x, y, selections=None):
    # Draws a layered character from bottom to top.

    if selections is None:
        selections = {}
    
    for part_name in LAYER_ORDER:
        part = sprites[part_name]

        if isinstance(part, list):
            selected_index = selections.get(part_name, 0)
            selected_sprite = part[selected_index]
        else:
            selected_sprite = part

        
        tk_image = ImageTk.PhotoImage(selected_sprite)

        canvas.create_image(x, y, image=tk_image)

        canvas.tk_images.append(tk_image)
