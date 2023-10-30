from pathlib import Path
from subprocess import run
from sys import platform

PROJ_DIR = Path(__file__).parents[0]
GUI = PROJ_DIR.joinpath("src", "GUI.py")
python = PROJ_DIR.joinpath(".venv", "bin", "python")
if platform == "win32":
    python = PROJ_DIR.joinpath(".venv", "Scripts", "python.exe")
run([python, GUI])
