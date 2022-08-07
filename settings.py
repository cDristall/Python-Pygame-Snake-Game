""" 
    File to hold all of the
     220805 v1 Snake Game's 
       GLOBAL CONSTANTS
"""
from os import path

# Name of the folder with all of the sprite, graphic, annd sound files
RESOURCE_FOLDER = "resources"


def get_file_path_name(file_name:str) -> str:
  """ Gets the absolute file path and returns it as a string. """
  cw_dir = path.dirname(__file__)
  full_path = path.join(cw_dir, RESOURCE_FOLDER, file_name)
  return full_path


# ----- Window Title -------
TITLE = "Snake"

# ---- Game Grid Dimensions ------
CELL_SIZE   = 40
GRID_WIDTH  = 17
GRID_HEIGHT = 15

# ----- Game Window Dimensions ------
SCREEN_WIDTH  = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)

# ------ Font Name --------
FONT_NAME = 'arial'

# ------ High Score File Name -------
HS_FILE = "high_score.txt"

# Graphic file paths (sprite pngs, sound effects, splash screens)
BG_IMAGE_PATH    = get_file_path_name("background_grid_680x600.png")
FOOD_IMAGE_PATH  = get_file_path_name("food_green_40x40.png")

# ----- Snake Head Images --------
HEAD_DOWN  = get_file_path_name("head_down.png")
HEAD_LEFT  = get_file_path_name("head_left.png")
HEAD_RIGHT = get_file_path_name("head_right.png")
HEAD_UP    = get_file_path_name("head_up.png")

# ------ Snake Tail Images --------
TAIL_DOWN  = get_file_path_name("tail_down.png")
TAIL_LEFT  = get_file_path_name("tail_left.png")
TAIL_RIGHT = get_file_path_name("tail_right.png")
TAIL_UP    = get_file_path_name("tail_up.png")


# ------ Snake Body Images --------
BODY_HORIZONTAL = get_file_path_name("body_horizontal.png")
BODY_VERTICAL   = get_file_path_name("body_vertical.png")

# ------ Snake Turning Body Image ------ 
TURN_DOWN_LEFT  = get_file_path_name("turn_down_left.png")
TURN_DOWN_RIGHT = get_file_path_name("turn_down_right.png")
TURN_UP_LEFT    = get_file_path_name("turn_up_left.png")
TURN_UP_RIGHT   = get_file_path_name("turn_up_right.png")

# ----- Sound Effects
HIT_SELF_SOUND = get_file_path_name("hit_self.wav")
HIT_FOOD_SOUND = get_file_path_name("hit_food.wav")

# ------ Define Colors ------
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)
GREEN    = (   0, 255,   0)
BLUE     = (   0,   0, 255)
# Set the BackGround Color
BGCOLOR  = BLACK
# ------ Other Colors ------
MAYA_BLUE  = ( 124, 185, 232)
ACID_GREEN = ( 176, 191,  26)

# Frames Per Second | Used to set the Frames Per Second speed
FPS_SPEED = 8