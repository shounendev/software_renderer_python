import pygame
import numpy as np
import time

from framebuffer import Framebuffer
from display_pygame import PygameDisplay
from pipeline import draw_mesh
from math3d import apply_matrix, rotation_x, rotation_y, normalize

WIDTH, HEIGHT = 300, 300

# cube vertices (homogeneous coords)
# vertices = np.array(
#     [
#         [-0.5, -0.5, -0.5, 1],
#         [0.5, -0.5, -0.5, 1],
#         [0.5, 0.5, -0.5, 1],
#         [-0.5, 0.5, -0.5, 1],
#         [-0.5, -0.5, 0.5, 1],
#         [0.5, -0.5, 0.5, 1],
#         [0.5, 0.5, 0.5, 1],
#         [-0.5, 0.5, 0.5, 1],
#     ]
# )

# face vertices
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
]

fb = Framebuffer(WIDTH, HEIGHT)
display = PygameDisplay(WIDTH, HEIGHT)

light_dir = normalize(np.array([0, 1, 1]))

running = True
angle_x = np.pi * 0.5
angle_y = 0.0

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    angle_y += 0.1
    M = np.matmul(rotation_y(angle_y), rotation_x(angle_x))

    fb.clear(0.0)
    draw_mesh(fb, vertices, faces, M, light_dir)
    display.draw(fb)

    clock.tick(30)
