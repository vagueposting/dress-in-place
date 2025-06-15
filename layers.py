from tkinter import *
from PIL import ImageTk, Image
from config import LAYER_ORDER, CHARACTER_POS_X, CHARACTER_POS_Y, GRADIENT_MAPPING
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
    # Get current sprites
    sprites = root.sprites
    
    # Apply gradients if they exist
    if hasattr(root, 'gradient_selections'):
        sprites = apply_gradients_to_sprites(sprites, 
                                             root.gradient_selections)
    # Draw character with current selections
    selections = getattr(root, 'selections', {})
    draw_character(canvas, sprites, CHARACTER_POS_X, 
                   CHARACTER_POS_Y, selections)
    
def apply_gradients_to_sprites(sprites, gradient_selections):
    if not gradient_selections:
        return sprites
        
    processed_sprites = {}
    for part_name, sprite in sprites.items():
        # Check if this part should use any gradient
        gradient_to_apply = None
        
        # First check for direct gradient assignment
        if part_name in gradient_selections:
            gradient_to_apply = gradient_selections[part_name]
        else:
            # Check if this is a body part that should use the body gradient
            for gradient_key, gradient_data in GRADIENT_MAPPING.items():
                if isinstance(gradient_data, dict) and 'parts' in gradient_data:
                    if part_name in gradient_data['parts'] and gradient_key in gradient_selections:
                        gradient_to_apply = gradient_selections[gradient_key]
                        break

        # Apply gradient if found
        if gradient_to_apply:
            if isinstance(sprite, list):
                processed_sprites[part_name] = [
                    apply_gradient(s, create_gradient_map(gradient_to_apply, size=(256, 1)))
                    for s in sprite
                ]
            else:
                processed_sprites[part_name] = apply_gradient(
                    sprite, 
                    create_gradient_map(gradient_to_apply, size=(256, 1))
                )
        else:
            processed_sprites[part_name] = sprite
            
    return processed_sprites