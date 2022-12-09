import pathlib
from calculator import Calculator

current_folder_path = pathlib.Path().resolve()
print("counting...")
Calculator.files()
