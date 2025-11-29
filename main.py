import pygame
import numpy as np
import time

from framebuffer import Framebuffer
from display_pygame import PygameDisplay
from display_ascii import AsciiDisplay
from pipeline import draw_mesh
from math3d import apply_matrix, rotation_x, rotation_y, normalize

WIDTH, HEIGHT = 40, 20

# cube vertices (homogeneous coords)
vertices = np.array(
    [
        [-0.5, -0.5, -0.5, 1],
        [+0.5, -0.5, -0.5, 1],
        [-0.5, -0.5, +0.5, 1],
        [+0.5, -0.5, +0.5, 1],
        [-0.5, +0.5, -0.5, 1],
        [+0.5, +0.5, -0.5, 1],
        [-0.5, +0.5, +0.5, 1],
        [+0.5, +0.5, +0.5, 1],
    ]
)

faces = [
    (0, 1, 2),
    (3, 2, 1),
    (6, 5, 4),
    (5, 6, 7),
    (7, 1, 5),
    (3, 1, 7),
    (0, 2, 4),
    (4, 2, 6),
    (4, 1, 0),
    (1, 4, 5),
    (2, 3, 6),
    (7, 6, 3),
]

scale = 1

scaleing_mat = [
    [scale, 0, 0, 0],
    [0, scale, 0, 0],
    [0, 0, scale, 0],
    [0, 0, 0, scale],
]

fb = Framebuffer(WIDTH, HEIGHT)
display = AsciiDisplay()

light_dir = normalize(np.array([0, -1, 1]))

running = True
angle_x = np.pi * 0.5
angle_y = 0.0

clock = pygame.time.Clock()
# hide terminal cursor
print("\033[?25l", end="", flush=True)

print("\033[?25l", end="")  # hide cursor

M = np.matmul(rotation_y(angle_y), rotation_x(angle_x))
print(M)
try:
    while running:
        angle_y += 0.1
        angle_x += -0.05
        M = np.matmul(rotation_y(angle_y), rotation_x(angle_x))
        M = np.matmul(M, scaleing_mat)

        fb.clear(0.0)
        draw_mesh(fb, vertices, faces, M, light_dir)
        display.draw(fb)

        clock.tick(30)

finally:
    print("Program is closing...")
    print("Restoring cursor visibility...")
    print("\033[?25h", end="", flush=True)
