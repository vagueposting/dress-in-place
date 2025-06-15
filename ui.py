from tkinter import *
from PIL import ImageTk, Image
from sprites import load_sprite
from config import *
from layers import redraw_character

def set_up(root):
    # Clear customization frame but preserve selections
    if hasattr(root, 'customization_frame'):
        root.customization_frame.destroy()
        del root.customization_frame
    
    # Redraw main menu
    canvas = root.canvas
    ui = root.ui
    
    # Redraw sidebar
    canvas.create_image(0, 0, anchor='nw', image=ui['bg'])
    canvas.create_image(0, 0, anchor='nw', image=ui['sidebar'])
    
    # Redraw character with current selections
    if hasattr(root, 'selections') and hasattr(root, 'gradient_selections'):
        redraw_character(canvas, root)
    
    # Redraw menu buttons
    root.main_menu_buttons = draw_menu(
        root, root.options, 
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
                 bg='white')
    frame.place(x=0, y=0)
    parent.customization_frame = frame

    # Back button
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
         text=f'{part_name}', 
         font=('Arial', 14),
         bg='white').place(x=20, y=60)

    # Create controls dynamically
    y_position = 100
    if part_name in CUSTOMIZATION_OPTIONS:
        for option_type, (label, options, part_key) in CUSTOMIZATION_OPTIONS[part_name].items():
            current_selection = 0  # Default to first option
            
            # For color options, find current selection if it exists
            if option_type == 'color' and hasattr(parent, 'gradient_selections'):
                current_gradient = parent.gradient_selections.get(part_key)
                if current_gradient and part_key in GRADIENT_MAPPING:
                    # Find which named gradient matches our current gradient
                    for name, gradient in GRADIENT_MAPPING[part_key].items():
                        if gradient == current_gradient:
                            try:
                                current_selection = options.index(name)
                            except ValueError:
                                current_selection = 0
                            break

            create_dropdown(
                frame, x=20, y=y_position,
                label=label,
                options=options,
                part_key=part_key,
                option_type=option_type,
                current_index=current_selection,
                canvas=parent.canvas,
                root=parent
            )
            y_position += 70

def create_dropdown(parent, x, y, label, options, part_key=None, option_type=None, current_index=0, canvas=None, root=None):
    Label(parent, text=label, bg='white').place(x=x, y=y)

    selected = StringVar(parent)
    selected.set(options[current_index] if current_index < len(options) else options[0])

    def on_change(*_):
        try:
            index = options.index(selected.get())
            
            if option_type == 'style':
                root.selections[part_key] = index
            elif option_type == 'color':
                if not hasattr(root, 'gradient_selections'):
                    root.gradient_selections = {}
                
                # Handle special body case
                if part_key == 'body':
                    gradient_name = selected.get()
                    root.gradient_selections['body'] = GRADIENT_MAPPING['body']['gradients'][gradient_name]
                else:
                    gradient_name = selected.get()
                    root.gradient_selections[part_key] = GRADIENT_MAPPING[part_key][gradient_name]

            redraw_character(canvas, root)
        except Exception as e:
            print(f"Error in dropdown change: {e}")

    selected.trace_add("write", on_change)

    dropdown = OptionMenu(parent, selected, *options)
    dropdown.config(bg='white')
    dropdown.place(x=x, y=y+30)

    return selected