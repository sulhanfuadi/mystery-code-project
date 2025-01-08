# import modules
import pygame
import numpy as np
from enigma_draw import *

# Set up the drawing window
W, H = 800, 800
screen = pygame.display.set_mode((H, W))
pygame.display.set_caption("di Bawah Alismu Hujan Berteduh, di Merah Matamu Senja Berlabuh") # If you don’t understand this text, just look it up—it’s really not that hard. Go on, give it a try!

# Set up the parameters
size_steps = 100
a = np.linspace(13, 13, size_steps)
b = np.linspace(-5, -3.3, size_steps)
c = np.linspace(-2, -2.4, size_steps)
d = np.linspace(-1, -0.16, size_steps)
scalex = np.linspace(1, 1.18, size_steps) * 10
scaley = np.linspace(1, 1.36, size_steps) * 10

# Create persitent particles
class PersistentParticle():
    def __init__(self, t, size, color, off_s):
        self.t = t
        self.off_s = off_s
        self.size = size
        self.color = color

    # Draw the particle
    def draw(self, screen: pygame.Surface, i):
        x, y = self.get_pos(i)
        draw_circle(screen, x, y, self.size, self.color)

    # Get the position of the particle
    def get_pos(self, i):
        t = self.t

        x_pos = 16 * np.sin(t) ** 3
        x_pos *= (scalex[i] + self.off_s)

        y_pos = a[i] * np.cos(t) + b[i] * np.cos(2*t) + c[i] * np.cos(3*t) + d[i] * np.cos(4*t)
        y_pos *= (scaley[i] + self.off_s)

        return int(x_pos + W / 2), int(-y_pos + H / 2)


class GlitterParticle():
    def __init__(self, t, size, color, off_x, off_y, off_s, phi):
        self.t = t
        self.off_x = off_x
        self.off_y = off_y
        self.off_s = off_s
        self.size = size
        self.color = color
        self.phi = phi

    # Get the position of the particle
    def get_pos(self, i):
        t = self.t

        x_pos = 16 * np.sin(t) ** 3
        x_pos += self.off_x
        x_pos *= (scalex[i] + self.off_s)

        y_pos = a[i] * np.cos(t) + b[i] * np.cos(2*t) + c[i] * np.cos(3*t) + d[i] * np.cos(4*t)
        y_pos += self.off_y
        y_pos *= (scaley[i] + self.off_s)

        return int(x_pos + W / 2), int(-y_pos + H / 2)

    # Draw the particle
    def draw(self, screen: pygame.Surface, i):
        x, y = self.get_pos(i)
        alpha = int(128 * np.cos(self.phi + i / 5) + 127)
        color = (self.color[0], self.color[1], self.color[2], alpha)
        draw_circle(screen, x, y, self.size, color)
