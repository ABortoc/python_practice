import os
import sys
import re
from PIL import Image

img_folder = sys.argv[1]
new_folder = sys.argv[2]

try:
    img_folder_path = fr".\{img_folder}"
    files = os.listdir(img_folder_path)
except FileNotFoundError:
    print("Specified directory does not exist. Task aborted")
    sys.exit()

if files:
    new_folder_path = fr".\{new_folder}"
    try:
        os.mkdir(new_folder_path)
    except:
        print(
            "New directory was not created. Directory with specified name already exists."
        )
        print("Continuing with the task without creating a new directory.")

    for img in files:
        file_name = re.match(r"(.*?)\.", img).group(1)
        Image.open(fr"{img_folder_path}\{img}").save(
            fr"{new_folder_path}\{file_name}.png"
        )
else:
    print("Specified directory is empty. Task aborted")
