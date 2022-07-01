# Importing the required Modules
import sys
import os
from PIL import Image

# Assigning the folders from the terminal
original_jpg_file = sys.argv[1]
converted_png_file = sys.argv[2]

# Checking if the new folder that stores the png file exists
if not os.path.exists(converted_png_file):
    # Creating the new folder if it does not exist
    os.makedirs(converted_png_file)

# Looping through the images in the folder storing the jpg images
for images in os.listdir(original_jpg_file):
    # Assigning the looped files to the variable below
    img = Image.open(f'{original_jpg_file}{images}')
    # Separating the image name from the image type
    separate_name = os.path.splitext(images)[0]
    # Assigning the new name and type of the image
    img.save(f'{converted_png_file}{separate_name}.png', 'png')
    # Just Confirming Everything Works :)
    print('All Done Fellas!!!')
