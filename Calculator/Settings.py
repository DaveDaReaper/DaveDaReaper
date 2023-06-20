# Size
APP_SIZE = (400, 700)
ROWS = 7
COLUMNS = 4

# Text
FONT = "Univers 55"
OUTPUT_FONT_SIZE = 70
MAIN_FONT_SIZE = 32

STYLING = {
    "gap": 0.5,
    "corner radius": 0}

NUMBER_POSITIONS = {
    ".": {"col": 2, "row": 6, "span": 1},
    0: {"col": 0, "row": 6, "span": 2},
    1: {"col": 0, "row": 5, "span": 1},
    2: {"col": 1, "row": 5, "span": 1},
    3: {"col": 2, "row": 5, "span": 1},
    4: {"col": 0, "row": 4, "span": 1},
    5: {"col": 1, "row": 4, "span": 1},
    6: {"col": 2, "row": 4, "span": 1},
    7: {"col": 0, "row": 3, "span": 1},
    8: {"col": 1, "row": 3, "span": 1},
    9: {"col": 2, "row": 3, "span": 1}}

MATH_POSITIONS = {
    "/": {"col": 3, "row": 2, "character": "/"},
    "*": {"col": 3, "row": 3, "character": "x"},
    "-": {"col": 3, "row": 4, "character": "-"},
    "+": {"col": 3, "row": 5, "character": "+"},
    "=": {"col": 3, "row": 6, "character": "="}}

OPERATORS = {
    "clear": {"col": 0, "row": 2, "text": "AC"},
    "invert": {"col": 1, "row": 2, "text": "INV"},
    "percent": {"col": 2, "row": 2, "text": "%"}}

COLOURS = {
    "light_grey": {"fg": ("#505050", "#D7D7D7"), "hover": ("#686868", "#EFEFEF"), "text": ("white", "black")},
    "dark_grey": {"fg": ("#D7D7D7", "#505050"), "hover": ("#EFEFEF", "#686868"), "text": ("black", "white")},
    "orange": {"fg": "#FA7D00", "hover": "#FF9500", "text": ("black", "white")},
    "orange_highlight": {"fg": "white", "hover": "white", "text": ("black", "#FA7D00")}}

TITLE_BAR_HEX_COLOURS = {
    "dark": 0x00000000,
    "light": 0x00EEEEEE}

BLACK = "#000000"
WHITE = "#EEEEEE"
