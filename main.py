import os
from pathlib import Path

from pico2d import *
import logo_mode
import game_framework

if __name__ == '__main__':
    os.chdir(Path(__file__).resolve().parent)
    open_canvas()
    try:
        game_framework.run(logo_mode)
    finally:
        close_canvas()
