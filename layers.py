from tkinter import *
from PIL import ImageTk, Image
from config import LAYER_ORDER, CHARACTER_POS_X, CHARACTER_POS_Y
from sprites import apply_gradient, create_gradient_map

def draw_character(canvas, sprites, x=CHARACTER_POS_X, 
                   y=CHARACTER_POS_Y, selections=None, tags="character"):
    # Draws a layered character from bottom to top.
    if selections is None:
        selections = {}

    # Clear existing character parts
    canvas.delete(tags)
    
    for part_name in LAYER_ORDER:
        part = sprites[part_name]

        if isinstance(part, list):
            selected_index = selections.get(part_name, 0)
            selected_sprite = part[selected_index]
        else:
            selected_sprite = part

        
        tk_image = ImageTk.PhotoImage(selected_sprite)

        canvas.create_image(x, y, image=tk_image, tags=tags)

        canvas.tk_images.append(tk_image)

def redraw_character(canvas, root):
    sprites = root.sprites

    # Apply gradient overrides if any
    if hasattr(root, 'gradient_selections') and root.gradient_selections:
        sprites = apply_gradients_to_sprites(sprites, root.gradient_selections)

    draw_character(canvas, sprites, 
                   CHARACTER_POS_X, CHARACTER_POS_Y, 
                   root.selections, 
                   tags="character")
    
def apply_gradients_to_sprites(sprites, gradient_map):
    modified = {}

    for key, sprite_list in sprites.items():
        if key in gradient_map:
            base_sprite = sprite_list[0]  # Use base image for gradient
            gradient_colors = gradient_map[key]

            # Create gradient map
            gradient = create_gradient_map(gradient_colors, size=(256, 1))

            # Apply gradient
            recolored = apply_gradient(base_sprite, gradient)
            modified[key] = [recolored] 

        else:
            modified[key] = sprite_list  # Keep original

    return modified