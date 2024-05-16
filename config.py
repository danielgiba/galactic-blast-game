import random

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCALE = 25
NUMBER_OF_ALIENS = 70
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
NUM_STARS = 100
STARS = [(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(NUM_STARS)]
