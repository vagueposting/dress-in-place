from tkinter import *
from PIL import ImageTk, Image
from sprites import load_sprite
from config import *
from layers import redraw_character

def set_up(root):
    # Clear any existing customization frame
    if hasattr(root, 'customization_frame'):
        root.customization_frame.destroy()
        del root.customization_frame
    
    # Get references from root
    canvas = root.canvas
    ui = root.ui
    options = root.options
    
    # Draw main menu buttons
    root.main_menu_buttons = draw_menu(
        root, options, 
        starting_x=SIDEBAR_MAX // 5,
        starting_y=CANVAS_HEIGHT // 6, 
        width_px=70,
        height_px=60, 
        gap_x=20, 
        gap_y=10
    )

def load_ui(sprite_name):
    return ImageTk.PhotoImage(load_sprite(sprite_name))

def draw_button(parent, text, x, y, width_px=70, height_px=60):
    btn = Button(
        parent,
        text=text,
        font=('Arial', 10),
        padx=width_px // 10,
        pady=height_px // 10,
        fg='black',
        bd=3,
        bg='#edbe6d',
        relief='flat',
        highlightthickness=2,
        highlightbackground='black',
        highlightcolor='black',
        borderwidth=2
    )
    btn.place(x=x, y=y)
    return btn

def draw_menu(parent, options, starting_x, starting_y, width_px, height_px, gap_x, gap_y):
    x = starting_x
    y = starting_y
    button_count = 0
    buttons = []

    for key in options:
        part_name = options[key]['name']
        
        btn = draw_button(parent, part_name, x, y, width_px, height_px)
        btn.config(command=lambda part=part_name: show_customize_screen(parent, part))
        buttons.append(btn)

        # Button positioning
        if button_count % 2 == 0:
            x += width_px + gap_x
        else:
            y += height_px + gap_y
            x = starting_x
        
        button_count += 1 
    
    return buttons

def show_customize_screen(parent, part_name):
    # Hide main menu buttons
    for btn in parent.main_menu_buttons:
        btn.place_forget()

    # Create customization panel
    frame = Frame(parent, 
                  width=SIDEBAR_MAX, 
                  height=CANVAS_HEIGHT,
                  bg='white')  # Match sidebar color
    frame.place(x=0, y=0)
    parent.customization_frame = frame

    # Back button - returns to main menu
    back_btn = Button(frame, text='← Back',
                      command=lambda: set_up(parent),
                      fg='black',
                      bd=2,
                      bg='#edbe6d',
                      relief='flat',
                      highlightthickness=2,
                      highlightbackground='black')
    back_btn.place(x=20, y=20)

    # Title
    Label(frame, 
          text=f'Customize: {part_name}', 
          font=('Arial', 14),
          bg='white').place(x=20, y=60)

    if part_name == 'Hairstyle':
        styles = ['Bob', 'Idol-inspired', 'Long', 'Pixie']
        colors = ['Blonde', 'Brunette', 'Redhead']
        create_dropdown(frame, x=20, y=100, label='Hairstyle', options=styles,
                        part_key='hair', canvas=parent.canvas, root=parent)
        create_dropdown(frame, x=20, y=170, label='Hair Color', options=colors,
                        part_key='hair', canvas=parent.canvas, root=parent)
    elif part_name == 'Eyes':
        styles = ['Tareme', 'Flat', 'Tsurime']
        colors = ['Blue', 'Brown', 'Green']
        create_dropdown(frame, x=20, y=100, label='Eye Style', options=styles,
                        part_key='eyes', canvas=parent.canvas, root=parent)
        create_dropdown(frame, x=20, y=170, label='Eye Color', options=colors)
    elif part_name == 'Mouth':
        styles = ['Smile', 'Meh', 'Frown']
        create_dropdown(frame, x=20, y=100, label='Mouth Style', options=styles,
                        part_key='mouth', canvas=parent.canvas, root=parent)

def create_dropdown(parent, x, y, label, options, part_key, canvas, root):
    Label(parent, text=label, bg='white').place(x=x, y=y)

    selected = StringVar(parent)
    selected.set(options[0])

    def on_change(*_):
        index = options.index(selected.get())
        gradient_colors = None

        # If it's a style (like "Hairstyle"), update sprite index
        if 'style' in label.lower():
            root.selections[part_key] = index
            # Clear any previous gradient override for this part
            if hasattr(root, 'gradient_selections'):
                root.gradient_selections[part_key] = index  # Optional fallback

        # If it's a color (like "Hair Color"), update gradient
        elif 'color' in label.lower():
            # Get the gradient based on selection
            if part_key == 'hair':
                gradient_colors = list(HAIR_GRADIENTS.values())[index]
            elif part_key == 'eyes':
                gradient_colors = list(EYE_GRADIENTS.values())[index]

            # Store gradient selection
            if not hasattr(root, 'gradient_selections'):
                root.gradient_selections = {}

            root.gradient_selections[part_key] = gradient_colors

        redraw_character(canvas, root)

    selected.trace_add("write", on_change)

    dropdown = OptionMenu(parent, selected, *options)
    dropdown.config(bg='white')
    dropdown.place(x=x, y=y+30)

    return selected