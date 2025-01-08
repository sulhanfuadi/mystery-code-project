# import module
import pygame
import numpy as np
from enigma_draw import *
from cryptic_particles import *
from colorsys import hsv_to_rgb

# initialize pygame
pygame.init()

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

persistent_particles = []
glitter_particles = []

# Create persitent particles
for repeat in range(3):
    for t in np.concatenate((np.linspace(0.18, 3.14-0.18, 1000), np.linspace(3.14+0.18, 2*3.1415-0.18, 1000)), axis=0):
        off_s = -np.random.exponential(1.8)
        size = int(rand(1.5, 2.5))
        
        # color
        red, green, blue = hsv_to_rgb(0.95, rand(0.2, 0.7), 1)
        alpha = np.random.rand() * 255
        color = (int(red * 255), int(green * 255), int(blue * 255), int(alpha))

        particle = PersistentParticle(t, size, color, off_s)
        persistent_particles.append(particle)

# Create glitter particles
for repeat in range(3):
    for t in np.concatenate((np.linspace(0.2, 3.14-0.2, 1000), np.linspace(3.14+0.2, 2*3.1415-0.2, 1000)), axis=0):
        off_x = np.random.randn() * 2
        off_y = np.random.randn() * 2
        off_s = np.random.randn() * 1.5 - 1.8
        size = int(rand(1.5, 2.5))
        
        # color
        red, green, blue = hsv_to_rgb(0.95, rand(0.5, 0.8), 1)
        color = (int(red * 255), int(green * 255), int(blue * 255))

        # phi
        phi = rand(0, 2*3.14)

        particle = GlitterParticle(t, size, color, off_x, off_y, off_s, phi)
        glitter_particles.append(particle)

# Set up the indices
bloom_indices = np.linspace(0, size_steps - 1, 40)
shrink_indices = np.linspace(size_steps - 1, 0, 30)
indices = np.concatenate((bloom_indices, shrink_indices), axis=0)
indices = np.uint8(indices)

# Set up the frame
frame = 0

# Run the program
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if the user closes the window
            running = False

    screen.fill((0, 0, 0)) # fill the screen with black

    index = indices[frame % len(indices)]
    for p in persistent_particles: # draw the persistent particles
        p.draw(screen, index)

    for p in glitter_particles:
        p.draw(screen, size_steps - 1 - index)

    frame += 1

    pygame.display.flip()

pygame.quit() # quit pygame, close the window