import pygame


class PygameDisplay:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))

    def draw(self, fb):
        surf = self.screen
        for y in range(fb.height):
            for x in range(fb.width):
                g = int(fb.pixels[y][x] * 255)
                surf.set_at((x, y), (g, g, g))
        pygame.display.flip()
