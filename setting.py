# Code by Chen Yufan
# Version 1
from typing import Union, Tuple, Sequence
import pygame
from pygame import Color

RGBAOutput = Tuple[int, int, int, int]
ColorValue = Union[Color, int, str, Tuple[int, int, int], RGBAOutput, Sequence[int]]

SCREEN_SIZE = (1000,800)
SCREEN_COLOR: ColorValue = 'Black'
TILE_SIZE = 50

clock = pygame.time.Clock()

black_bg = pygame.Surface((1000, 800))
black_bg.fill('Black')
