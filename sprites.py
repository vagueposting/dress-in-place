from tkinter import *
from PIL import ImageTk, Image
import numpy as np

def load_sprite(part_name):
    pil_image = Image.open(f'img/small/{part_name}.png').convert('RGBA')
    return pil_image

def load_sprite_batch(part_name, number_of_opts):
    sprite_array = []
    for i in range(number_of_opts):
        sprite_array.append(load_sprite(f'{part_name}{i+1}'))
    return sprite_array

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_gradient_map(colors, size=(256,1)):
    # Create a horizontal gradient image from the list of colors
    img = Image.new('RGB', (len(colors), 1))
    pixels = img.load()
    for i, color in enumerate(colors):
        rgb = hex_to_rgb(color)
        pixels[i, 0] = rgb
    return img.resize(size, resample=Image.BILINEAR)

def apply_gradient(sprite, gradient):
    # Load sprite in RGBA mode to preserve transparency
    sprite = sprite.convert('RGBA')

    # Split into color and alpha channels
    r, g, b, a = sprite.split()
    luminance = np.array(r)  # Use red channel as grayscale proxy
    alpha = np.array(a)

    # Get gradient array and reshape
    gradient_array = np.array(gradient)[0]  # Shape: (256, 3)

    # Normalize luminance to [0, 255] then map to gradient index
    index_map = (luminance / 255.0 * (gradient_array.shape[0] - 1)).astype(np.uint8)

    # Create empty RGB arrays for output
    recolored_r = np.zeros_like(luminance)
    recolored_g = np.zeros_like(luminance)
    recolored_b = np.zeros_like(luminance)

    # Fill them using the gradient only where alpha > 0
    mask = alpha > 0
    recolored_r[mask] = gradient_array[index_map[mask], 0]
    recolored_g[mask] = gradient_array[index_map[mask], 1]
    recolored_b[mask] = gradient_array[index_map[mask], 2]

    # Combine back into final RGBA image
    recolored_r = Image.fromarray(recolored_r)
    recolored_g = Image.fromarray(recolored_g)
    recolored_b = Image.fromarray(recolored_b)

    recolored_image = Image.merge('RGB', (recolored_r, recolored_g, recolored_b))
    final_image = Image.new('RGBA', sprite.size)
    final_image.paste(recolored_image, mask=Image.fromarray(alpha))

    return final_image