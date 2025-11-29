class Framebuffer:
    def __init__(self, width, heigt):
        self.width = width
        self.heigt = height
        self.pixels = [[0.0 for _ in range(width)] for _ in range(heigt)]

    def clear(self, value=0.0):
        for y in range(self.heigt):
            for x in range(self.width):
                self.pixels[y][x] = value

    def set_pixel(self, x, y, value):
        if x >= 0 and x < self.width and y >= 0 and y < self.heigt:
            self.pixels[y][x] = value
