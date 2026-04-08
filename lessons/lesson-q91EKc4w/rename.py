import os
import pathlib

files = pathlib.Path(".").glob("*")

for file in files:
    if file.is_file():
        new_name = file.name.replace("lesson1", "lesson-q91EKc4w")
        file.rename(new_name)
        print(f"Renamed {file.name} to {new_name}")

