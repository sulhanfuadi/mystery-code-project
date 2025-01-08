# import modules
import pygame
import pygame.gfxdraw
import numpy as np

# draw a circle, filled, on the screen
def draw_circle(screen, x, y, r, color):
    pygame.gfxdraw.filled_circle(screen, x, y, r, color)

# generate a random number between a0 and a1, inclusive
def rand(a0, a1):
    return np.random.rand() * (a1 - a0) + a0