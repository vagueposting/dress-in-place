import os
import re

# Set the folder path where your images are located
folder_path = 'img/shrunken'

# Regular expression pattern to match the prefix
pattern = re.compile(r'^fullres_\d+s_\d+_(.*)$')

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    match = pattern.match(filename)
    if match:
        # Extract the part after the prefix
        new_name = match.group(1)
        
        # Get full paths
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        print(f'Renamed: {filename} -> {new_name}')