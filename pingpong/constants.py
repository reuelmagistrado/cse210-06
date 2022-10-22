from game.casting.color import Color

# --------------------------------------------------------------------------------------------------
# GENERAL GAME CONSTANTS
# --------------------------------------------------------------------------------------------------

# GAME
GAME_NAME = "Ping Pong"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "pingpong/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "pingpong/assets/sounds/boing.wav"
WELCOME_SOUND = "pingpong/assets/sounds/start.wav"
OVER_SOUND = "pingpong/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
UP = "up"
UP2 = "w"
DOWN = "down"
DOWN2 = "s"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = "pingpong/assets/data/level-{:03}.txt"
BASE_LEVELS = 5

# --------------------------------------------------------------------------------------------------
# SCRIPTING CONSTANTS
# --------------------------------------------------------------------------------------------------

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# --------------------------------------------------------------------------------------------------
# CASTING CONSTANTS
# --------------------------------------------------------------------------------------------------

# STATS
STATS_GROUP = "stats"
MAXIMUM_ROUND = 10

# HUD
HUD_MARGIN = 15
PLAYER1_GROUP = "player1"
PLAYER2_GROUP = "player2"
ROUND_GROUP = "round"
PLAYER1_FORMAT = "Player 1: {}"
PLAYER2_FORMAT = "Player 2: {}"
ROUND_FORMAT = "Round: {}"

# BALL
BALL_GROUP = "balls"
BALL_IMAGE = "pingpong/assets/images/000.png"
BALL_WIDTH = 28
BALL_HEIGHT = 28
BALL_VELOCITY = 10

# RACKET
RACKET_GROUP = "rackets"
RACKET_IMAGES = [f"pingpong/assets/images/{n:03}.png" for n in range(100, 103)]
RACKET2_IMAGES = [
    f"pingpong/assets/images/{n:03}.png" for n in range(103, 106)]
RACKET_WIDTH = 106
RACKET_HEIGHT = 28
RACKET_RATE = 6
RACKET_VELOCITY = 7

# BRICK
BRICK_GROUP = "bricks"
BRICK_IMAGES = {
    "b": [f"pingpong/assets/images/{i:03}.png" for i in range(10, 19)],
    "g": [f"pingpong/assets/images/{i:03}.png" for i in range(20, 29)],
    "p": [f"pingpong/assets/images/{i:03}.png" for i in range(30, 39)],
    "y": [f"pingpong/assets/images/{i:03}.png" for i in range(40, 49)]
}
BRICK_WIDTH = 80
BRICK_HEIGHT = 28
BRICK_DELAY = 0.5
BRICK_RATE = 4
BRICK_POINTS = 50

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"
