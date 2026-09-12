# Converts the videos into mp3

import os
import subprocess

files = os.listdir("videos")

for file in files:

    if "Part-" in file:
        tutorial_number = file.split("Part-")[1].split(" ")[0]
        new_name = f"c language video{tutorial_number}.mp3"
        print(new_name)
        input_file = os.path.join("videos", file)
        
        subprocess.run(["ffmpeg","-i",input_file",new_name])

    else:
        print("Skipped:", file)
        